from app import app ,logging, STATUS,db
from model import *
from utils import *
from flask import jsonify, request, sessions

import os

import json
import cv2
import pytesseract
import math

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Indium Software\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#img = cv2.imread('pan_originapng.png')

#img = cv2.imread('pan_dup.png')

from pytesseract import Output

import datetime

import io
import re

#pan_number = 'DMKPP3104B'

#pan_number = '(OMKPP3104B'

IMAGE_PATH = "C:\\Users\\Indium Software\\Documents\\develop\\document_proof\\images"

@app.route("/")
def home():
    logging.info("start")
    return "Document Proof API Services"

def allowed_file(filename):
    return '.' in filename and \
           (filename.rsplit('.', 1)[1]).lower() in ["pdf", "jpg", "jpeg", "png"]  

@app.route("/user-proof", methods=['POST'])
def user_proof():
    logging.info("user_proof : Start")
    resp_dict={"status":False,"msg":None,"object":None}
    try:
        user_seq_no = 1
        if user_seq_no > 0:
            id_image = request.files['image']
            input_json = json.load(request.files['inputs'])
            if id_image:
                str_time =  datetime.datetime.now().strftime('%d%m%Y%H%M%S')
                image_file_name = str_time+".jpg"
                
                logging.info(os.path.isdir(IMAGE_PATH))
                if os.path.isdir(IMAGE_PATH)==False:
                    os.mkdir(IMAGE_PATH)
                    
                id_image.save(os.path.join(IMAGE_PATH,image_file_name))
                
                id_image = cv2.imread(IMAGE_PATH+"/"+image_file_name)
                
                config_obj =  Config.query.filter(Config.id_type == input_json["id_type"]).all()
                
                if input_json["id_type"] == "pan":
                    verified = verify_pan(config_obj,id_image,image_file_name,input_json["id_number"],input_json["dob"])
                else:
                    print("Id Type Required")
                    
                proof_dict={"image_originality":True, "score":verified}
                if verified > 70:
                    resp_dict["msg"] = "Genuine id card"
                    resp_dict["status"] = True
                    resp_dict["object"] = proof_dict
                else:
                    resp_dict["msg"] = "Verification Needed"
                    resp_dict["object"] = verified  
                    
        else:
            resp_dict["msg"] = "Session Expired"
 
    except Exception as e:
        logging.exception("user_proof : exception : {}".format(e))
        resp_dict["msg"] = "Internal Server Error"
    resp = jsonify(resp_dict)
    logging.debug("user_proof : end")
    return resp

def verify_pan(config_obj, img,image_file_name,pan_number,dob): 
    logging.info("verify_pan : Start")
    try:
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        n_boxes = len(d['level'])
        for i in range(n_boxes):
            if(d['text'][i] != ""):
                #dept
                if (d['text'][i] == 'DEPARTMENT'):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    department = (x, y, w, h)
                    logging.info(f"department:{department}")
                #govt
                if (d['text'][i] == 'GOVT.'):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    govt = (x, y, w, h)
                    logging.info(f"govt:{govt}")
                #permanent
                if (d['text'][i] == 'Permanent'):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    permanent = (x, y, w, h)
                    logging.info(f"permanent:{permanent}")
                #pan number   
                if (d['text'][i] == pan_number):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    pan_number = (x, y, w, h)
                    logging.info(f"pan_number:{pan_number}")
                #father
                #if (d['text'][i] != "" ) and (d['text'][i].startswith('Father')):
                if (d['text'][i] == "Father's"):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    father = (x, y, w, h)
                    logging.info(f"father:{father}")
                # date 
                if (d['text'][i] == 'Date'):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    date = (x, y, w, h)
                    logging.info(f"date:{date}")
                # date of birth  
                if (d['text'][i] == dob):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    dob = (x, y, w, h)
                    logging.info(f"dob:{dob}")
                    
        # Dept vs Govt co-ordinates
        dept_x1 = department[0]
        dept_y1 = department[1]
        govt_x2 = govt[0]
        govt_y2 = govt[1]
        dept_gov_dist = math.sqrt((govt_x2 - dept_x1)**2 + (govt_y2 - dept_y1)**2)
        dept_gov_dist = round(dept_gov_dist,4)
        logging.info(f"dept_gov_dist:{dept_gov_dist}")

        dept_width = department[2]
        dept_height = department[3]

        govt_width = govt[2]
        govt_height = govt[3]
                
        dept_ratio = (dept_width/dept_height) 
        dept_ratio = round(dept_ratio,4)
        logging.info(f"dept_ratio:{dept_ratio}")

        govt_ratio = govt_width/govt_height 
        govt_ratio = round(govt_ratio,4)
        logging.info(f"govt_ratio:{govt_ratio}")
                
        # Per vs Pan_number co-ordinates       
        per_x1 = permanent[0]
        per_y1 = permanent[1]
        pan_number_x2 = pan_number[0]
        pan_number_y2 = pan_number[1]
        per_pan_dist = math.sqrt((pan_number_x2 - per_x1)**2 + (pan_number_y2 - per_y1)**2)
        per_pan_dist = round(per_pan_dist,4)
        logging.info(f"per_pan_dist:{per_pan_dist}") 

        per_width = permanent[2]
        per_height = permanent[3]

        pan_number_width = pan_number[2] 
        pan_number_height = pan_number[3]
                
        per_ratio = (per_width/per_height) 
        per_ratio = round(per_ratio,4)
        logging.info(f"per_ratio:{per_ratio}")

        pan_number_ratio = pan_number_width/pan_number_height
        pan_number_ratio = round(pan_number_ratio,4)
        logging.info(f"pan_number_ratio:{pan_number_ratio}")
                            
        # Father vs Date co-ordinates       
        father_x1 = father[0]
        father_y1 = father[1]
        date_x2 = date[0]
        date_y2 = date[1]
        father_date_dist = math.sqrt((date_x2 - father_x1)**2 + (date_y2 - father_y1)**2)
        father_date_dist = round(father_date_dist,4)
        logging.info(f"father_date_dist:{father_date_dist}")

        father_width = father[2]
        father_height = father[3]

        date_width = date[2]
        date_height = date[3]
                
        father_ratio = (father_width/father_height) 
        father_ratio = round(father_ratio,4)
        logging.info(f"father_ratio:{father_ratio}")

        date_ratio = date_width/date_height
        date_ratio = round(date_ratio,4)
        logging.info(f"date_ratio:{date_ratio}")
        
        datee_x1 = date[0]
        datee_y1 = date[1]
        dob_x2 = dob[0]
        dob_y2 = dob[1]
        date_dob_dist = math.sqrt((dob_x2 - datee_x1)**2 + (dob_y2 - datee_y1)**2)
        date_dob_dist = round(date_dob_dist,4)
        logging.info(f"date_dob_dist:{date_dob_dist}")

        datee_width = date[2]
        datee_height = date[3]

        dob_width = dob[2]
        dob_height = dob[3]
                
        datee_ratio = (datee_width/datee_height)
        datee_ratio = round(datee_ratio,4)
        logging.info(f"datee_ratio:{datee_ratio}")

        dob_ratio = dob_width/dob_height
        dob_ratio = round(dob_ratio,4)
        logging.info(f"dob_ratio:{dob_ratio}")

        dept_govt_accuracy = 0
        per_pan_accuracy = 0
        father_date_accuracy = 0
        date_dob_accuracy = 0
        
        for config in config_obj:
            d=config.id_params
            d=json.loads(d)
            print(type(d['dept_gov_dist']))

            #print(d)
            if dept_gov_dist == d['dept_gov_dist'] and dept_ratio == d['dept_ratio'] and govt_ratio == d['govt_ratio']:
                dept_govt_accuracy = 20
            else:
                dept_govt_accuracy = 0
                
            logging.info(f"dept_govt_accuracy:{dept_govt_accuracy}")
                
            if per_pan_dist == d['per_pan_dist'] and per_ratio == d['per_ratio'] and pan_number_ratio == d['pan_number_ratio']:
                per_pan_accuracy = 20
            else:
                per_pan_accuracy = 0
                
            logging.info(f"per_pan_accuracy:{per_pan_accuracy}")
                
            if father_date_dist == d['father_date_dist'] and father_ratio == d['father_ratio'] and date_ratio == d['date_ratio']:
                father_date_accuracy = 20
            else:
                father_date_accuracy = 0
                
            logging.info(f"father_date_accuracy:{father_date_accuracy}")
                
            if date_dob_dist == d['date_dob_dist'] and datee_ratio == d['date_ratio'] and dob_ratio == d['dob_ratio']:
                date_dob_accuracy = 20
            else:
                date_dob_accuracy = 0
                
            logging.info(f"date_dob_accuracy:{date_dob_accuracy}")
                
            id_seq = Config.query.all()
            for id in id_seq:
                seq_id = id.seq_id
                
            total_score = dept_govt_accuracy + per_pan_accuracy+ father_date_accuracy + date_dob_accuracy
            document = Document(image_file_name,seq_id,total_score)
            db.session.add(document)
            db.session.commit()
            
            return total_score
                  
    except Exception as e:
        logging.exception("verify_pan : exception : {}".format(e))
    logging.debug("verify_pan : end")
    return 0

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5001)
 