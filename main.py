import serial #Import serial library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button as mat_but
 

arduinoSerialData = serial.Serial('/dev/ttyACM0',57600)

class UserForm(object):
	"""docstring for UserForm"""
	def __init__(self, root):
		super(UserForm, self).__init__()
		self.root = root
		self.user_dict = {}
		self.commodities = None

		root.title("Practikum : Neuroprosthetics")
		root.geometry("1000x1000")
		

		Largelabel = LabelFrame(root,text="Force measurement Device",bg="#ccccff")
		Largelabel.pack(fill="both",expand="yes")


		heading = Label(Largelabel,text="Finger force measurement Device", fg = "black",bg = "#ccccff", font = "Oswald 25 bold italic")
		heading.place(x= 500, y=50,anchor='c')

		# User form
		name_label = Label(Largelabel ,text = "Name :",font = "Oswald 15 bold",bg="#ff9999").place(x=100,y=200)
		email_label = Label(Largelabel ,text = "Email Id :",font = "Oswald 15 bold",bg="#ff9999").place(x=100,y=250) 
		age_label = Label(Largelabel ,text = "Age :",font = "Oswald 15 bold",bg="#ff9999").place(x=100,y=300) 
		biosex_label = Label(Largelabel ,text = "Biological Sex :",font = "Oswald 15 bold",bg="#ff9999").place(x=100,y=350)
		fingers_label = Label(Largelabel ,text = "Fingers :",font = "Oswald 15 bold",bg="#ff9999").place(x=100,y=400)   

		name_entry = Entry(Largelabel,font=15)
		name_entry.place(x=350,y=200)
		email_entry = Entry(Largelabel,font=15)
		email_entry.place(x=350,y=250)
		age_entry = Entry(Largelabel,font=15)
		age_entry.place(x=350,y=300)

		vari = IntVar()
		R1 = Radiobutton(Largelabel, text="Male",bg="#ccccff", variable=vari, value=1,command=self.sel,font=15)
		R2 = Radiobutton(Largelabel, text="Female",bg="#ccccff", variable=vari, value=2,command=self.sel,font=15)
		R3 = Radiobutton(Largelabel, text="Other",bg="#ccccff", variable=vari, value=3,command=self.sel,font=15)
		R1.place(x=350,y=350)
		R2.place(x=450,y=350)
		R3.place(x=550,y=350)
		
		var1 = IntVar()
		var2 = IntVar()
		var3 = IntVar()
		var4 = IntVar()
		var5 = IntVar()

		c1 = Checkbutton(Largelabel, text='Little finger',bg="#ccccff",variable=var1, onvalue=1, offvalue=0, command=self.sel)
		c1.place(x=350,y=400)
		c2 = Checkbutton(Largelabel, text='Ring finger',bg="#ccccff",variable=var2, onvalue=1, offvalue=0, command=self.sel)
		c2.place(x=350,y=420)
		c3 = Checkbutton(Largelabel, text='Middle finger',bg="#ccccff",variable=var3, onvalue=1, offvalue=0, command=self.sel)
		c3.place(x=350,y=440)
		c4 = Checkbutton(Largelabel, text='Index finger',bg="#ccccff",variable=var4, onvalue=1, offvalue=0, command=self.sel)
		c4.place(x=350,y=460)
		c5 = Checkbutton(Largelabel, text='Thumb',bg="#ccccff",variable=var5, onvalue=1, offvalue=0, command=self.sel)
		c5.place(x=350,y=480)

		description = Text(Largelabel, height = 20, width = 40).place(x=350,y =550)
		Add_label = Label(Largelabel ,text = "Additional details :",font = "Oswald 15 bold",bg="#ff9999").place(x=100,y=550)

		self.commodities = [var1,var2,var3,var4,var5,vari,name_entry,email_entry,age_entry,description]
		button_submit = Button(Largelabel, bg="#34e1eb", text ="Submit", font = "Oswald 20 bold", command = self.gather_data)
		button_submit.place(x = 430, y=800)
		root.mainloop()

	def sel(self):
	   print ("Selection came here")

	def gather_data(self):
		self.user_dict["add_descrip"] = self.commodities[0].get()
		self.user_dict["user_age"] = self.commodities[8].get()
		self.user_dict["user_email"] = self.commodities[7].get()
		self.user_dict["user_name"] = self.commodities[6].get()

		self.user_dict["fingers"] = []
		for i in range(0,5):
			self.user_dict["fingers"].append(self.commodities[i].get())

		self.user_dict["sex"] = self.commodities[5].get()

		self.root.destroy()


class OptionsForm(object):
	"""docstring for OptionsForm"""
	def __init__(self, currform):
		super(OptionsForm, self).__init__()
		self.currform = currform
		self.current_op = None
		self.currform.title("Practikum : Neuroprosthetics")
		self.currform.geometry("1000x1000")

		Largelabel = LabelFrame(self.currform,text="Force measurement Device",bg="#ccccff")
		Largelabel.pack(fill="both",expand="yes")

		heading = Label(Largelabel,text="Finger force measurement Device", fg = "black",bg = "#ccccff", font = "Oswald 25 bold italic")
		heading.place(x= 500, y=50,anchor='c')

		button_calib = Button(Largelabel, bg="#34e1eb", text ="Calibration", font = "Oswald 20 bold", command = lambda: self.get_button_text(button_calib))
		button_calib.place(x = 250, y=350)

		button_measurement = Button(Largelabel, bg="#34e1eb", text ="Force measurement", font = "Oswald 20 bold", command = lambda: self.get_button_text(button_measurement))
		button_measurement.place(x = 250, y=450)

		button_stat = Button(Largelabel, bg="#34e1eb", text ="Statistics", font = "Oswald 20 bold", command = lambda: self.get_button_text(button_stat))
		button_stat.place(x = 250, y=550)



		
		image1 = Image.open("/home/anas/Desktop/code/courses/neuro/project_code/resources/pngegg.png")
		image1 = image1.resize((80, 80))
		image1_wid = ImageTk.PhotoImage(image1)
		label1 = Label(Largelabel, bg = "#ccccff",image=image1_wid)
		label1.place(x=610,y=330)

		image2 = Image.open("/home/anas/Desktop/code/courses/neuro/project_code/resources/force_m.png")
		image2 = image2.resize((100, 100))
		image2_wid = ImageTk.PhotoImage(image2)
		label2 = Label(Largelabel, bg = "#ccccff",image=image2_wid)
		label2.place(x=600,y=430)

		image3 = Image.open("/home/anas/Desktop/code/courses/neuro/project_code/resources/statistics.png")
		image3 = image3.resize((100, 100))
		image3_wid = ImageTk.PhotoImage(image3)
		label3 = Label(Largelabel, bg = "#ccccff",image=image3_wid)
		label3.place(x=600,y=530)

		self.currform.mainloop()

	def get_button_text(self,button):
		if "Calibration" == button["text"]:
			self.current_op = 0
		elif "Force measurement" == button["text"]:
			self.current_op = 1
		else:
			self.current_op = 2

		self.currform.destroy()



class Calib_form(object):
	"""docstring for Calib_form"""
	def __init__(self, form):
		super(Calib_form, self).__init__()
		self.form = form
		self.form.title("Practikum : Neuroprosthetics")
		self.form.geometry("1000x1000")
		Largelabel = LabelFrame(self.form,text="Force measurement Device",bg="#ccccff")
		Largelabel.pack(fill="both",expand="yes")


		self.offset = {"little" :[0,0],"ring":[0,0],"middle":[0,0],"index":[0,0],"thumbx":[0,0],"thumby":[0,0]}

		print ("Starting with the Calibration")
		self.label1 = Label(Largelabel ,text = "Calibration",font = "Oswald 20 bold",bg="#ccccff").place(x=400,y=200)
		self.label2 = Label(Largelabel ,text = "Starting weight calibration",font = "Oswald 15 italic",bg="#ccccff")
		self.label2.place(x=50,y=300)


		self.form.after(1000, self.offset_calculation)

		self.form.mainloop()

	
	def add_string(self,total_text,new_txt):

		if "|" in new_txt:
			split_data = new_txt.split("|")
			print (split_data)
			if split_data[1] in total_text.keys():
				print ("it did eneter")
				if len(total_text[split_data[1]]) == 0:
					total_text[split_data[1]] = split_data[0]

		total_bool = True
		for i in total_text.keys():
			total_bool= (len(total_text[i]) > 0) and total_bool


		return total_text, total_bool 


	def offset_calculation(self):
		print ("Please remove any weights from the finger pieces. There should be no object place closed to the wire. Please press Yes")
		self.label2.config(text="Please remove any weights from the finger pieces. \nThere should be no object place closed to the wire. Please press Yes")
		answer = messagebox.askyesno("Question", "Please remove any weights from the finger pieces. There should be no object place closed to the wire. Please press Yes after you have so")
		if answer:
			# code for calculating the offset
			total_count = 0
			total_text = {"little" :"","ring":"","middle":"","index":"","thumbx":"","thumby":""}
			exit_cond = False
			while True:
				if (arduinoSerialData.inWaiting()>0):
					myData = arduinoSerialData.readline()
					total_text,all_m = self.add_string(total_text,str(myData)[2:-5])
					if all_m:
						for i in total_text.keys():
							self.offset[i][0] = int(total_text[i])
							exit_cond = True
						break
				if exit_cond:
					break;

		else:
			self.form.destroy()
		

		print (self.offset)
		for key in self.offset.keys():
			answer = messagebox.askyesno("Question", f"Please place a 0.5 kg weight on top of the finger{key} piece.\nPlease press Yes after it.")          
			self.label2.config(text=f"Please place a 0.5 kg weight on top of the finger{key} piece.\nPlease press Yes after it.")
			if answer :
				total_count = 0
				total_text = {"little" :"","ring":"","middle":"","index":"","thumbx":"","thumby":""}
				exit_cond = False
				while True:
					if (arduinoSerialData.inWaiting()>0):
						myData = arduinoSerialData.readline()
						total_text,all_m = self.add_string(total_text,str(myData)[2:-5])
						if all_m:
							for i in total_text.keys():
								self.offset[i][1] = (int(total_text[i]) - self.offset[i][1]) / 5
								exit_cond = True
							break
					if exit_cond:
						break

			else:
				print ("Exiting the calibration...")


		d_str = json.dumps(self.offset)
		self.label2.config(text=("These are the calibration parameters:"+d_str))
		with open('data/calib_param.json', 'w') as f:
			json.dump(self.offset, f)
		messagebox.showinfo("Calibration parameters", d_str)
		self.form.destroy()



class Measurment_form(object):
	"""docstring for Measurment_form"""
	def __init__(self,user_dict):
		super(Measurment_form, self).__init__()
		self.user_dict = user_dict
		self.sine_wave = []
		self.fing_f = {"little" :[0] * 200,"ring":[0] * 200,"middle":[0] * 200,"index":[0] * 200,"thumbx":[0] * 200,"thumby":[0] * 200}

		plt.ion()
		fig = plt.figure(figsize=(15, 10))
		self.ref_fig = fig
		x = np.linspace(0., 5., 100)
		y = np.sin(x)

		rows = 6
		columns = 2

		grid = plt.GridSpec(rows, columns, wspace = .25, hspace = .25)
		line_fig = {}
		count = 0
		

		ax1 = plt.subplot(grid[0, 0])
		plt.annotate("Little", xy = (10, -5), va = 'center', ha = 'center',  weight='bold', fontsize = 7.5)
		ax1.set_xlim(0,200)
		ax1.set_ylim(-20,20)
		line1 = plt.plot(x,y)

		ax1 = plt.subplot(grid[1, 0])
		plt.annotate("Ring", xy = (10, -5), va = 'center', ha = 'center',  weight='bold', fontsize = 7.5)
		ax1.set_xlim(0,200)
		ax1.set_ylim(-20,20)
		line2 = plt.plot(x,y)

		ax1 = plt.subplot(grid[2, 0])
		plt.annotate("Middle", xy = (10, -5), va = 'center', ha = 'center',  weight='bold', fontsize = 7.5)
		ax1.set_xlim(0,200)
		ax1.set_ylim(-20,20)
		line3 = plt.plot(x,y)

		ax1 = plt.subplot(grid[3, 0])
		plt.annotate("Index", xy = (10, -5), va = 'center', ha = 'center',  weight='bold', fontsize = 7.5)
		ax1.set_xlim(0,200)
		ax1.set_ylim(-20,20)
		line4 = plt.plot(x,y)

		ax1 = plt.subplot(grid[4, 0])
		plt.annotate("Thumbx", xy = (10, -5), va = 'center', ha = 'center',  weight='bold', fontsize = 7.5)
		ax1.set_xlim(0,200)
		ax1.set_ylim(-20,20)
		line5 = plt.plot(x,y)

		ax1 = plt.subplot(grid[5, 0])
		plt.annotate("Thumby", xy = (10, -5), va = 'center', ha = 'center',  weight='bold', fontsize = 7.5)
		ax1.set_xlim(0,200)
		ax1.set_ylim(-20,20)
		line6 = plt.plot(x,y)


		plt.subplot(grid[0:3, 1])
		plt.annotate('Sine Wave: \nPlease flex and extend accordingly', xy = (0.75, -0.5), va = 'center', ha = 'center',  weight='bold', fontsize = 10)
		sine_line = plt.plot(x, y)

		ax7 =plt.subplot(grid[3:6, 1])
		annotation = plt.annotate('Total Force', xy = (30, 5), va = 'center', ha = 'center',  weight='bold', fontsize = 10)
		ax7.set_xlim(0,200)
		ax7.set_ylim(-40,40)
		total_output = [0] * 200
		total_force = plt.plot(range(0,200), total_output)

		button_ax = plt.axes([0.8, 0.0125, 0.1, 0.05])
		button = mat_but(button_ax, 'Save and Close')       
		button.on_clicked(self.save_plot)
		total_text = {"little" :"","ring":"","middle":"","index":"","thumbx":"","thumby":""}
		
		self.save_and_close = False
		import time
		offset = None
		with open('data/calib_param.json', 'r') as file:
			offset = json.load(file)

		while True:
			if self.save_and_close:
				button.on_clicked(self.save_plot)
				break
			if (arduinoSerialData.inWaiting()>0):
				myData = arduinoSerialData.readline()
				if "$" not in str(myData):
					total_text,all_m = self.add_string(total_text,str(myData)[2:-5])
					if all_m:
						for curr_key in total_text.keys():
							if curr_key == "little" :
								self.fing_f[curr_key].append((int(total_text[curr_key])-offset[curr_key][0])/offset[curr_key][1])
								self.fing_f[curr_key].pop(0)
								line1[0].set_xdata(range(len(self.fing_f[curr_key])))
								line1[0].set_ydata(self.fing_f[curr_key])
								print ("little",self.fing_f[curr_key])
							elif curr_key == "ring" :
								self.fing_f[curr_key].append((int(total_text[curr_key])-offset[curr_key][0])/offset[curr_key][1])
								self.fing_f[curr_key].pop(0)
								line2[0].set_xdata(range(len(self.fing_f[curr_key])))
								line2[0].set_ydata(self.fing_f[curr_key])
								print ("ring",self.fing_f[curr_key]) 
							elif curr_key == "middle" :
								self.fing_f[curr_key].append((int(total_text[curr_key])-offset[curr_key][0])/offset[curr_key][1])
								self.fing_f[curr_key].pop(0)
								line3[0].set_xdata(range(len(self.fing_f[curr_key])))
								line3[0].set_ydata(self.fing_f[curr_key])
								print ("middle",self.fing_f[curr_key]) 
							elif curr_key == "index" :
								self.fing_f[curr_key].append(-1*(int(total_text[curr_key])-offset[curr_key][0])/offset[curr_key][1])
								self.fing_f[curr_key].pop(0)
								line4[0].set_xdata(range(len(self.fing_f[curr_key])))
								line4[0].set_ydata(self.fing_f[curr_key])
								print ("index",self.fing_f[curr_key])
							elif curr_key == "thumbx" :
								self.fing_f[curr_key].append((int(total_text[curr_key])-offset[curr_key][0])/offset[curr_key][1])
								self.fing_f[curr_key].pop(0)
								line5[0].set_xdata(range(len(self.fing_f[curr_key])))
								line5[0].set_ydata(self.fing_f[curr_key])
								print ("middle",self.fing_f[curr_key])
							elif curr_key == "thumby" :
								self.fing_f[curr_key].append(-1*(int(total_text[curr_key])-offset[curr_key][0])/offset[curr_key][1])
								self.fing_f[curr_key].pop(0)
								line6[0].set_xdata(range(len(self.fing_f[curr_key])))
								line6[0].set_ydata(self.fing_f[curr_key])
								print ("middle",self.fing_f[curr_key])

						count +=1
						total_text = {"little" :"","ring":"","middle":"","index":"","thumbx":"","thumby":""}
						

						newy = np.sin(x-0.125*count)
						sine_line[0].set_xdata(x)
						sine_line[0].set_ydata(newy)

						total_text_final = "Total Force \n"
						final_value = 0.0
						for curr_key in total_text.keys():
							final_value = final_value + np.abs(self.fing_f[curr_key][200-1])
						total_output.append(final_value)
						total_output.pop(0)
						for curr_key in total_text.keys():
							total_text_final = total_text_final + curr_key + ": "+str(np.abs(self.fing_f[curr_key][200-1]) * 100/final_value) +"%\n"
						
						annotation.set_text(total_text_final)
						total_force[0].set_xdata(list(range(0,200)))
						total_force[0].set_ydata(total_output)
						


				fig.canvas.draw()
				fig.canvas.flush_events()
				time.sleep(0.01)
			else:
				fig.canvas.draw()
				fig.canvas.flush_events()
				time.sleep(0.01)

		count = 0


	def add_string(self,total_text,new_txt):

		if "|" in new_txt:
			split_data = new_txt.split("|")
			if split_data[1] in total_text.keys():
				if len(total_text[split_data[1]]) == 0:
					total_text[split_data[1]] = split_data[0]

		total_bool = True
		for i in total_text.keys():
			total_bool= (len(total_text[i]) > 0) and total_bool


		return total_text, total_bool 


	def save_plot(self,event):
		print ("close all matplotlib figures")
		final_dict = {"user_infomation":self.user_dict,"force_measurements":self.fing_f}
		with open(("data/"+self.user_dict["user_name"]+".json"), "w") as file:
			json.dump(final_dict, file)
		self.save_and_close = True


class Stats_form(object):
	"""docstring for Stats_form"""
	def __init__(self, form):
		super(Stats_form, self).__init__()
		self.form = form
						



def main():

	root = Tk()
	main_window = UserForm(root)
	user_dict = main_window.user_dict

	options = Tk()
	options_window = OptionsForm(options)
	option = options_window.current_op
	print ("option choosen : ",option)

	if option == 0:
		print ("calibration window")
		calibration = Tk()
		calibration_window = Calib_form(calibration)
	elif option==1:
		print ("Force measurement frame")
		measure_window = Measurment_form(user_dict)


	else:
		print ("Statistics")


if __name__ == '__main__':
	main()