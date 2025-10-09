from PySide6 import QtCore , QtGui , QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

class MyStylToolDialog(QtWidgets.QDialog) :
	def __init__(self,parent = None) :
		super().__init__(parent)

		self.setWindowTitle('Advance Camera Helper Tool')
		self.resize(700,500)

		#เปลี่ยนาีbackground
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
                background-color: black ;
			'''
			)

		

		self.nameLayout  = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)

		self.inputInfoLayout = QtWidgets.QGridLayout()
		self.mainLayout.addLayout(self.inputInfoLayout)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)



		#ui
		#หัวข้อแรก

		self.CameraCreationNameLabel = QtWidgets.QLabel('Camera Creation')
		self.CameraCreationNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 20px ;
					color : white ;
					font-family: "Mollen Trial";
					font-weight : bold ;
					
				}
			'''
			)

		self.CameraNameNameLabel = QtWidgets.QLabel('Camera Name :')
		self.CameraNameNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
					
					
				}
			'''
			)

		self.CameraNameNameLineEdit = QtWidgets.QLineEdit()
		self.CameraNameNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					 } 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.FocalLengthNameLabel = QtWidgets.QLabel('Focal Length :')
		self.FocalLengthNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
					
					
				}
			'''
			)
		self.FocalLengthNameLineEdit = QtWidgets.QLineEdit()
		self.FocalLengthNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )
		
		self.CreatCameraButton = QtWidgets.QPushButton('Create Camera')
		self.CreatCameraButton.setStyleSheet(
			'''
				QPushButton {
					background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                                stop:0 #5B5A54, 
                                                stop:1 #8A8463);
					color : black ;
					border-radius : 10px ;
					font-size : 16 ;
					padding : 10px ;
					font-family: "Mollen Trial";


				}


			'''
			)

		#หัวข้อสอง

		self.CameraMovementNameLabel = QtWidgets.QLabel('Camera Movement')
		self.CameraMovementNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 20px ;
					color : white ;
					font-family: "Mollen Trial";
					font-weight : bold ;
					
					
				}
			'''
			)

		self.PanSildeLabel = QtWidgets.QLabel('Pan')
		self.PanSildeLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
					
					
				}
			'''
			)
		self.PanSildeCombobox = QtWidgets.QComboBox()
		self.PanSildeCombobox.setStyleSheet(
			'''
				QComboBox {
                	color: white; 
               		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                                stop:0 #5B5A54, 
                                                stop:1 #8A8463);
			'''
			)

		self.DollySildeLabel = QtWidgets.QLabel('Dolly')
		self.DollySildeLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
					
					
				}
			'''
			)
		self.DollySildeCombobox = QtWidgets.QComboBox()
		self.DollySildeCombobox.setStyleSheet(
			'''
				QComboBox {
                	color: white; 
               		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                                stop:0 #5B5A54, 
                                                stop:1 #8A8463);
			'''
			)

		self.PanSpeedNameLabel = QtWidgets.QLabel('Pan Speed :')
		self.PanSpeedNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
					
					
				}
			'''
			)
		self.PanSpeedNameLineEdit = QtWidgets.QLineEdit()
		self.PanSpeedNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.DollySpeedNameLabel = QtWidgets.QLabel('Dolly Speed :')
		self.DollySpeedNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
					
					
				}
			'''
			)
		self.DollySpeedNameLineEdit = QtWidgets.QLineEdit()
		self.DollySpeedNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.SetKeyButton = QtWidgets.QPushButton('Set Key Frame')
		self.SetKeyButton.setStyleSheet(
			'''
				QPushButton {
					background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                                stop:0 #5B5A54, 
                                                stop:1 #8A8463);
					color : black ;
					border-radius : 10px ;
					font-size : 16 ;
					padding : 10px ;
					font-family: "Mollen Trial";

				}


			'''
			)

		#หัวข้อสาม

		self.CameraShakeNameLabel = QtWidgets.QLabel('Camera Shake Generator')
		self.CameraShakeNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 20px ;
					color : white ;
					font-family: "Mollen Trial";
					font-weight : bold ;
					
					
				}
			'''
			)

		self.IntensityNameLabel = QtWidgets.QLabel('Intensity :')
		self.IntensityNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
											
				}
			'''
			)
		self.IntensityNameLineEdit = QtWidgets.QLineEdit()
		self.IntensityNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.DurationNameLabel = QtWidgets.QLabel('Duration : ')
		self.DurationNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
											
				}
			'''
			)

		self.DurationNameLineEdit = QtWidgets.QLineEdit()
		self.DurationNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.StarFrameNameLabel = QtWidgets.QLabel('StarFrame : ')
		self.StarFrameNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
											
				}
			'''
			)
		self.StarFrameNameLineEdit = QtWidgets.QLineEdit()
		self.StarFrameNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.EndFrameNameLabel = QtWidgets.QLabel('EndFrame : ')
		self.EndFrameNameLabel.setStyleSheet(
			'''
				QLabel {
					width: 120px;
					height: 48px;
					font-size : 11px ;
					color : white ;
					font-family: "Mollen Trial";
											
				}
			'''
			)
		self.EndFrameNameLineEdit = QtWidgets.QLineEdit()
		self.EndFrameNameLineEdit.setStyleSheet(
			'''
				 QLineEdit { 

                    border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: #383732;
					} 
                	
                QLineEdit:focus { 
                	border-radius: 10px; 
                    border-style:outset;
                    border-width:2px;
                    border-radius: 4px;
                    border-color: white;

					color:rgb(0, 0, 0); 
                	background-color: white; 
            	} 
                    
            '''
           )

		self.SetKeyTwoButton = QtWidgets.QPushButton('Set Key Frame')
		self.SetKeyTwoButton.setStyleSheet(
			'''
				QPushButton {
					background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                                stop:0 #5B5A54, 
                                                stop:1 #8A8463);
					color : black ;
					border-radius : 10px ;
					font-size : 16 ;
					padding : 10px ;
					font-family: "Mollen Trial";

				}


			'''
			)


		#addwidget--------
		#หัวข้อแรก

		self.inputInfoLayout.addWidget(self.CameraCreationNameLabel,0,0,1,0)

		self.inputInfoLayout.addWidget(self.CameraNameNameLabel,1,0)
		self.inputInfoLayout.addWidget(self.CameraNameNameLineEdit,1,1)

		self.inputInfoLayout.addWidget(self.FocalLengthNameLabel,2,0)
		self.inputInfoLayout.addWidget(self.FocalLengthNameLineEdit,2,1)

		self.inputInfoLayout.addWidget(self.CreatCameraButton,3,0,1,0) #ทำปุ่มตรงกลาง

		#หัวข้อสอง

		self.inputInfoLayout.addWidget(self.CameraMovementNameLabel,4,0)

		self.inputInfoLayout.addWidget(self.PanSildeLabel,5,0)
		self.inputInfoLayout.addWidget(self.PanSildeCombobox,5,1)

		self.inputInfoLayout.addWidget(self.DollySildeLabel,6,0)
		self.inputInfoLayout.addWidget(self.DollySildeCombobox,6,1)

		self.inputInfoLayout.addWidget(self.PanSpeedNameLabel,7,0)
		self.inputInfoLayout.addWidget(self.PanSpeedNameLineEdit,7,1)

		self.inputInfoLayout.addWidget(self.DollySpeedNameLabel,8,0)
		self.inputInfoLayout.addWidget(self.DollySpeedNameLineEdit,8,1)

		self.inputInfoLayout.addWidget(self.SetKeyButton,9,0,1,0)

		#หัวข้อสาม

		self.inputInfoLayout.addWidget(self.CameraShakeNameLabel,10,0)

		self.inputInfoLayout.addWidget(self.IntensityNameLabel,11,0)
		self.inputInfoLayout.addWidget(self.IntensityNameLineEdit,11,1)

		self.inputInfoLayout.addWidget(self.DurationNameLabel,12,0)
		self.inputInfoLayout.addWidget(self.DollySpeedNameLineEdit,12,1)

		self.inputInfoLayout.addWidget(self.StarFrameNameLabel,13,0)
		self.inputInfoLayout.addWidget(self.StarFrameNameLineEdit,13,1)

		self.inputInfoLayout.addWidget(self.EndFrameNameLabel,14,0)
		self.inputInfoLayout.addWidget(self.EndFrameNameLineEdit,14,1)

		self.inputInfoLayout.addWidget(self.SetKeyTwoButton,15,0,1,0)


		#ดันuiขึ้น
		self.mainLayout.addStretch()



def run() :
	global ui 
	try :
		ui.close()
	except :
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = MyStylToolDialog(parent=ptr)
	ui.show()