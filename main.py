import csv
import os
import shutil
import sys

import numpy as np
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QIntValidator, QKeySequence
from PySide2.QtWidgets import QApplication, QDial, QDialog, QMainWindow, QMessageBox, QWidget, QLabel, QCheckBox, QFileDialog, QDesktopWidget, QLineEdit, \
    QRadioButton, QShortcut, QScrollArea, QVBoxLayout, QGroupBox, QFormLayout, QPushButton
from xlsxwriter.workbook import Workbook

from ui.main_window import Ui_main_window
from ui.labeler_widget import Ui_labeler_widget
from ui.new_dialog import Ui_new_dialog
from ui.open_dialog import Ui_open_dialog
from functools import partial

from rc import resource

def get_img_paths(dir, extensions=('.jpg', '.png', '.jpeg')):
    '''
    :param dir: folder with files
    :param extensions: tuple with file endings. e.g. ('.jpg', '.png'). Files with these endings will be added to img_paths
    :return: list of all filenames
    '''

    img_paths = []

    for filename in os.listdir(dir):
        if filename.lower().endswith(extensions):
            img_paths.append(os.path.join(dir, filename))

    return img_paths


def make_folder(directory):
    """
    Make folder if it doesn't already exist
    :param directory: The folder destination path
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


class New_Dialog(Ui_new_dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # State variables
        self.selected_folder = ''
        self.mode = 'csv'
        self.label_values = []
        self.img_paths = []

        # UI update
        self.numLabelsInput.setValidator(QIntValidator(self.numLabelsInput))
        self.scroll_area_widget.setLayout(QFormLayout(self.scroll_area_widget))

        # Connect
        self.browse_button.clicked.connect(self.pick_folder_images)
        self.confirm_num_labels.clicked.connect(self.generate_label_inputs)
        self.buttonBox.accepted.connect(self.continue_app)

        self.csv_radioButton.clicked.connect(partial(self.mode_changed, "csv"))
        self.copy_radioButton.clicked.connect(partial(self.mode_changed, "copy"))
        self.move_radioButton.clicked.connect(partial(self.mode_changed, "move"))


    def mode_changed(self, mode: str):
        """
        Sets new mode (one of: csv, copy, move)
        """
        self.mode = mode
 
    def pick_folder_images(self):
        """
        shows a dialog to choose folder with images to label
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=QFileDialog.ShowDirsOnly|QFileDialog.DontUseNativeDialog)

        self.selected_folder_label.setText(folder_path)
        self.selected_folder = folder_path

    def generate_label_inputs(self):
        """
        Generates input fields for labels. The layout depends on the number of labels.
        """

        # check that number of labels is not empty
        if self.numLabelsInput.text().isnumeric():
            num_labels = int(self.numLabelsInput.text())

            while self.scroll_area_widget.layout().rowCount() > 0:
                self.scroll_area_widget.layout().removeRow(0)

            for i in range(num_labels):
                self.scroll_area_widget.layout().addRow(QLabel(f'label {i + 1}:', self), QLineEdit(self))

    def check_validity(self):
        """
        :return: if all the necessary information is provided for proper run of application. And error message
        """
        if self.selected_folder == '':
            return False, 'Input folder has to be selected.'

        num_labels_input = self.numLabelsInput.text().strip()
        if num_labels_input == '' or num_labels_input == '0':
            return False, 'Number of labels has to be number greater than 0.'

        if self.scroll_area_widget.layout().rowCount()== 0:
            return False, "You didn't provide any labels. Select number of labels and press \"Ok\""

        for i in range(self.scroll_area_widget.layout().rowCount()):
            item_field = self.scroll_area_widget.layout().itemAt(i, QFormLayout.FieldRole).widget()

            if item_field.text().strip() == '':
                return False, 'All label fields has to be filled.'

        self.img_paths = get_img_paths(self.selected_folder)
        if len(self.img_paths) == 0:
            return False, 'Input folder has no photos.'

        return True, 'Form ok'

    def continue_app(self):
        """
        If the setup form is valid, the Labeler_Widget is opened and all necessary information is passed to it
        """
        form_is_valid, message = self.check_validity()

        if form_is_valid:
            self.label_values = []
            for i in range(self.scroll_area_widget.layout().rowCount()):
                item_field = self.scroll_area_widget.layout().itemAt(i, QFormLayout.FieldRole).widget()
                self.label_values.append(item_field.text().strip())

            self.accept()
        else:
            QMessageBox.warning(self, "Warning", message)

class Open_Dialog(Ui_open_dialog, QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.img_paths = []

        self.openfolder_button.clicked.connect(self.pick_images_folder)
        self.opencsv_button.clicked.connect(self.pick_csv_file)
        self.buttonBox.accepted.connect(self.continue_app)

    def pick_images_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=QFileDialog.ShowDirsOnly|QFileDialog.DontUseNativeDialog)

        self.selected_folder_label.setText(folder_path)

    def pick_csv_file(self):
        csv_path, _ = QFileDialog.getOpenFileName(self, "Select csv", filter="csv files (*.csv)", options=QFileDialog.DontUseNativeDialog)
        self.selected_csv_label.setText(csv_path)

    def check_validity(self):
        """
        :return: if all the necessary information is provided for proper run of application. And error message
        """
        if self.selected_folder_label.text() == '':
            return False, "Empty folder path."

        if self.selected_csv_label.text() == '':
            return False, "Empty csv path."

        self.img_paths = get_img_paths(self.selected_folder_label.text())
        if len(self.img_paths) == 0:
            return False, "The folder has no photo."

        self.accept()
        return True, "Form is ok"

    def continue_app(self):
        """
        If the setup form is valid, the Labeler_Widget is opened and all necessary information is passed to it
        """
        form_is_valid, message = self.check_validity()

        if form_is_valid:
            self.accept()
        else:
            QMessageBox.warning(self, "Warning", message)

class Labeler_Widget(Ui_labeler_widget, QWidget):
    def __init__(self, labels, input_folder, img_paths, mode):
        super().__init__()
        self.setupUi(self)

        # state variables
        self.counter = 0
        self.input_folder = input_folder
        self.img_paths = img_paths
        self.labels = labels
        self.assigned_labels = {}
        self.mode = mode

        # initialize list to save all label buttons
        self.label_buttons = []

        # create label folders
        if mode == 'copy' or mode == 'move':
            self.create_label_folders(labels, self.input_folder)

        # init UI
        self.init_ui()

    def init_ui(self):
        
        self.init_buttons()

        # show image
        self.set_image(self.img_paths[0])

        # image name
        self.img_name_label.setText(self.img_paths[self.counter])

        # progress bar
        self.progress_bar.setText(f'image 1 of {len(self.img_paths)}')

    def init_buttons(self):

        self.prev_im_btn.clicked.connect(self.show_prev_image)
        self.next_im_btn.clicked.connect(self.show_next_image)

        # Add "Prev Image" and "Next Image" keyboard shortcuts
        prev_im_kbs = QShortcut(QKeySequence("p"), self)
        prev_im_kbs.activated.connect(self.show_prev_image)

        next_im_kbs = QShortcut(QKeySequence("n"), self)
        next_im_kbs.activated.connect(self.show_next_image)

        # Add "generate csv file" button
        self.generate_csv_btn.clicked.connect(partial(self.generate_csv, 'assigned_classes'))

        # Create button for each label
        x_shift = 0  # variable that helps to compute x-coordinate of button in UI
        y_shift = 0
        for i, label in enumerate(self.labels):
            self.label_buttons.append(QPushButton(label, self))
            button = self.label_buttons[i]

            # create click event (set label)
            button.clicked.connect(partial(self.set_label, label))

            # create keyboard shortcut event (set label)
            # shortcuts start getting overwritten when number of labels >9
            label_kbs = QShortcut(QKeySequence(f"{i+1 % 10}"), self)
            label_kbs.activated.connect(partial(self.set_label, label))

            # place button in GUI (create multiple columns if there is more than 10 button)
            if y_shift > self.image_box.height():
                x_shift += 120
                y_shift = 0

            button.move(self.image_box.geometry().topRight().x() + 20 + x_shift, self.image_box.y() + y_shift)
            y_shift += 40

    def set_label(self, label):
        """
        Sets the label for just loaded image
        :param label: selected label
        """
        # get image filename from path (./data/images/img1.jpg → img1.jpg)
        img_path = self.img_paths[self.counter]
        img_name = os.path.split(img_path)[-1]

        # if the img has some label already
        if img_name in self.assigned_labels.keys():

            # label is already there = means tht user want's to remove label
            if label in self.assigned_labels[img_name]:
                self.assigned_labels[img_name].remove(label)

                # remove key from dictionary if no labels are assigned to this image
                if len(self.assigned_labels[img_name]) == 0:
                    self.assigned_labels.pop(img_name, None)

                # remove image from appropriate folder
                if self.mode == 'copy':
                    os.remove(os.path.join(self.input_folder, label, img_name))

                elif self.mode == 'move':
                    # label was in assigned labels, so I want to remove it from label folder,
                    # but this was the last label, so move the image to input folder.
                    # Don't remove it, because it it not save anywehre else
                    if img_name not in self.assigned_labels.keys():
                        shutil.move(os.path.join(self.input_folder, label, img_name), self.input_folder)
                    else:
                        # label was in assigned labels and the image is store in another label folder,
                        # so I want to remove it from current label folder
                        os.remove(os.path.join(self.input_folder, label, img_name))

            # label is not there yet. But the image has some labels already
            else:
                self.assigned_labels[img_name].append(label)

                # path to copy/move images
                copy_to = os.path.join(self.input_folder, label)

                # copy/move the image into appropriate label folder
                if self.mode == 'copy':
                    # the image is stored in input_folder, so i can copy it from there (differs from 'move' option)
                    shutil.copy(img_path, copy_to)

                elif self.mode == 'move':
                    # the image doesn't have to be stored in input_folder anymore.
                    # get the path where the image is stored
                    copy_from = os.path.join(self.input_folder, self.assigned_labels[img_name][0], img_name)
                    shutil.copy(copy_from, copy_to)

        else:
            # Image has no labels yet. Set new label and copy/move

            self.assigned_labels[img_name] = [label]
            # move copy images to appropriate directories
            copy_to = os.path.join(self.input_folder, label)

            if self.mode == 'copy':
                shutil.copy(img_path, copy_to)
            elif self.mode == 'move':
                shutil.move(img_path, copy_to)

        # load next image
        if self.show_next_checkbox.isChecked():
            self.show_next_image()
        else:
            self.set_button_color(img_name)

    def show_next_image(self):
        """
        loads and shows next image in dataset
        """
        if self.counter < len(self.img_paths) - 1:
            self.counter += 1

            path = self.img_paths[self.counter]
            filename = os.path.split(path)[-1]

            # If we have already assigned label to this image and mode is 'move', change the input path.
            # The reason is that the image was moved from '.../input_folder' to '.../input_folder/label'
            if self.mode == 'move' and filename in self.assigned_labels.keys():
                path = os.path.join(self.input_folder, self.assigned_labels[filename][0], filename)

            self.set_image(path)
            self.img_name_label.setText(path)
            self.progress_bar.setText(f'image {self.counter + 1} of {len(self.img_paths)}')
            self.set_button_color(filename)
            # self.csv_generated_message.setText('')


        # change button color if this is last image in dataset
        elif self.counter == len(self.img_paths) - 1:
            path = self.img_paths[self.counter]
            self.set_button_color(os.path.split(path)[-1])

    def show_prev_image(self):
        """
        loads and shows previous image in dataset
        """
        if self.counter > 0:
            self.counter -= 1

            if self.counter < len(self.img_paths):
                path = self.img_paths[self.counter]
                filename = os.path.split(path)[-1]

                # If we have already assigned label to this image and mode is 'move', change the input path.
                # The reason is that the image was moved from '.../input_folder' to '.../input_folder/label'
                if self.mode == 'move' and filename in self.assigned_labels.keys():
                    path = os.path.join(self.input_folder, self.assigned_labels[filename][0], filename)

                self.set_image(path)
                self.img_name_label.setText(path)
                self.progress_bar.setText(f'image {self.counter + 1} of {len(self.img_paths)}')

                self.set_button_color(filename)
                # self.csv_generated_message.setText('')

    def set_image(self, path):
        """
        displays the image in GUI
        :param path: relative path to the image that should be show
        """

        pixmap = QPixmap(path)
        self.image_box.setPixmap(pixmap)

    def generate_csv(self, out_filename):
        """
        Generates and saves csv file with assigned labels.
        Assigned label is represented as one-hot vector.
        :param out_filename: name of csv file to be generated
        """
        path_to_save = os.path.join(self.input_folder, 'output')
        make_folder(path_to_save)
        csv_file_path = os.path.join(path_to_save, out_filename) + '.csv'

        with open(csv_file_path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')

            # write header
            writer.writerow(['img'] + self.labels)

            # write one-hot labels
            for img_name, labels in self.assigned_labels.items():
                labels_one_hot = self.labels_to_zero_one(labels)
                writer.writerow([img_name] + list(labels_one_hot))

        message = f'csv saved to: {csv_file_path}'
        # self.csv_generated_message.setText(message)
        # print(message)

        if self.generate_xlsx_checkbox.isChecked():
            try:
                self.csv_to_xlsx(csv_file_path)
            except:
                print('Generating xlsx file failed.')

    def csv_to_xlsx(self, csv_file_path):
        """
        converts csv file to xlsx file
        :param csv_file_path: path to csv file which we want to convert to lsx
        """
        workbook = Workbook(csv_file_path[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()

        with open(csv_file_path, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)

        workbook.close()

    def set_button_color(self, filename):
        """
        changes color of button which corresponds to selected label
        :filename filename of loaded image:
        """

        if filename in self.assigned_labels.keys():
            assigned_labels = self.assigned_labels[filename]
        else:
            assigned_labels = []

        for button in self.label_buttons:
            if button.text() in assigned_labels:
                button.setStyleSheet('border: 1px solid #43A047; background-color: #4CAF50; color: white')
            else:
                button.setStyleSheet('background-color: None')

    def closeEvent(self, event):
        """
        This function is executed when the app is closed.
        It automatically generates csv file in case the user forgot to do that
        """
        print("closing the App..")
        self.generate_csv('assigned_classes_automatically_generated')

    def labels_to_zero_one(self, labels):
        """
        Convert number to one-hot vector
        :param number: number which represents for example class index
        :param num_classes: number of classes in dataset so I know how long the vector should be
        :return:
        """

        # create mapping from label name to its index for better efficiency {label : int}
        label_to_int = dict((c, i) for i, c in enumerate(self.labels))

        # initialize array to save selected labels
        zero_one_arr = [0]* len(self.labels)
        for label in labels:
            zero_one_arr[label_to_int[label]] = 1

        return zero_one_arr

    @staticmethod
    def create_label_folders(labels, folder):
        for label in labels:
            make_folder(os.path.join(folder, label))



class Main_Window(Ui_main_window, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icon.png"))
        
        self.new_dialog = New_Dialog()
        self.open_dialog = Open_Dialog()
        self.labeler_widget: Labeler_Widget = None

        self.assigned_labels = {}

        self.action_new.triggered.connect(self.process)
        self.action_open.triggered.connect(self.process)
        self.action_about.triggered.connect(self.process)

    def process(self):
        if self.sender() == self.action_new:
            ret = self.new_dialog.exec()
            if ret == QDialog.Accepted:
                if self.labeler_widget is not None:
                    self.labeler_widget.deleteLater()
                self.labeler_widget = Labeler_Widget(self.new_dialog.label_values, self.new_dialog.selected_folder, self.new_dialog.img_paths, self.new_dialog.mode)
                self.setCentralWidget(self.labeler_widget)

        elif self.sender() == self.action_open:
            ret = self.open_dialog.exec()
            if ret == QDialog.Accepted:
                selected_folder = self.open_dialog.selected_folder_label.text()
                selected_csv = self.open_dialog.selected_csv_label.text()

                with open(selected_csv) as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    firstrow = next(reader)
                    labels = firstrow[1:]

                    if self.labeler_widget is not None:
                        self.labeler_widget.deleteLater()
                    self.labeler_widget = Labeler_Widget(labels, selected_folder, self.open_dialog.img_paths, 'csv')

                    for row in reader:
                        img_name = row[0]
                        label_digits = row[1:]
                        image_path = os.path.join(selected_folder, img_name)

                        if image_path in self.labeler_widget.img_paths:
                            for i, label_digit in enumerate(label_digits):
                                if label_digit == "1":
                                    if img_name not in self.labeler_widget.assigned_labels:
                                        self.labeler_widget.assigned_labels[img_name] = [labels[i]]
                                    else:
                                        self.labeler_widget.assigned_labels[img_name].append(labels[i])

                self.setCentralWidget(self.labeler_widget)

        elif self.sender() == self.action_about:
            QMessageBox.information(self, "About", "<h3>Khiem Tran</h3><br/><p>Image annotation tool</p>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())
