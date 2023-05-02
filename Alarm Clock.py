from datetime import datetime
import playsound
        
def validator(alarm_time):
    if len(alarm_time) > 12:
        return "Invalid input format"
    else:
        if int(alarm_time[:2]) > 59:
            return "Invalid Hour format"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid minute format"
        elif int(alarm_time[6:8]) > 59:
            return "Invalid seconds format"
        else:
            return 'ok'
          
while True:
    try:
        alarm_time = input("Enter time format HH:MM:SS AM/PM ")
        validate = validator(alarm_time)
        if validate != 'ok':
            print(validate)
        else:
            print("Setting alarm for {}...".format(alarm_time))
            break
    except Exception:
        print("Invalid input format")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_alarm_pm = now.strftime("%p")
        
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5] 
    alarm_seconds = alarm_time[6:8]
    alarm_pm = alarm_time[9:].upper()
        
    if alarm_hour == current_hour:
        if alarm_minute == current_minute:
            if alarm_seconds == current_second:
                if alarm_pm == current_alarm_pm:
                    print("timeup!")
                    playsound.playsound('C:\\Users\\USER\\Downloads\\alert2.wav')
                    break
        
        
        
            
        
                
            
            