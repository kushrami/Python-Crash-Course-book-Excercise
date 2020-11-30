#Cars:

def car_details(manufacturer, model_name, **Other_info):

    car_detail = {}

    car_detail['manufacturer'] = manufacturer
    car_detail['model name'] = model_name

    for key,value in Other_info.items():
        car_detail[key] = value
    
    return car_detail

car = car_details('subaru', 'outback', color='blue', tow_package=True)
print(car)