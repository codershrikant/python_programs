import json
    # key:value mapping

# def demo_of_decoding_encoding():
#     import demjson
#     # pip install demjson
#     # syntax: demjson.encode(self,obj,nest_level = 0) 
#     a = [{"Name": 'Peter',"Age":20, "Subject":"Electronics"}]  
#     print(demjson.encode(a))  


def pprint_demo():
    person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}' 
    per_dict = json.loads(person) 
    print(json.dumps(per_dict, indent=5, sort_keys= False))

def mix_data_type():
    a = ["Mathew", "Peter", (10, 32.9, 80), {"Name":"Tokyo"}]
    # python object into JSON
    b = json.dumps(a)
    print(b)
    # json into python object
    c = json.loads(b)
    print(c)


def deserialized_file_to_python_object():
    student = {
        "Name" : "Peter",
        "Roll_no" : "0090014",
        "Grade" : "A",
        "Age" : 20,
    }

    with open("static/json/data.json", "w") as write_file:
        json.dump(student, write_file)

    with open("static/json/data.json", "r") as read_file:
        b = json.load(read_file)
    print(b)


def data_type_to_json():
    """
    JSON Serialization:
    dict = object
    list, tuple = Array
    Str = String
    int, float = Number
    True, False = true, false
    None = null

    JSON Deserialization
    Object = dict
    Array = list
    String = str
    number(int) = int
    true, false = True, False
    null = None
    """
    print("Python list conversion to JSON Array")
    print(json.dumps(['Welecome', 'to', 'Inheritance Infosystem']),"\n")

    print("Python tuple conversion to JSON Array")
    print(json.dumps(('Welecome', 'to', 'Inheritance Infosystem')),"\n")

    print("Python string conversion to JSON String")
    print(json.dumps('Inheritance Infosystem'),"\n")

    print("Python int conversion to JSON Number")
    print(json.dumps(1234),"\n")

    print("Python float conversion to JSON Number")
    print(json.dumps(23.572),"\n")

    print("Python boolean conversion to JSON boolean")
    print(json.dumps(True),"\n")

    print("Python boolean conversion to JSON boolean")
    print(json.dumps(False),"\n")

    print("Python None conversion to JSON null")
    print(json.dumps(None),"\n")


def object_are_not_same_after_conversion_to_return():
    a = (10, 20, 30, 40, 50, 60, 70)
    print(type(a))
    b = json.dumps(a)
    print(type(json.loads(b)))


def dic_to_json_demo():
    """
        prints simple dict into the form of json data
        args: none
        returns: none
    """
    student = {
            "Name": "Peter",
            "Roll_no" : "0090014",
            "Grade" : "A",
            "Age" : 20
        }    

    b = json.dumps(student)
    print(b)




if __name__ == '__main__':
    pprint_demo()