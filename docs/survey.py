def survey1():
    answer={}
    question=["What is your first name?  ","What is your last name?  ", "How old are you?  ", "What is your birthday? Format in MM/DD/YY  ","How much time do you spend on your phone? Type the following options: A little, average, or often."]
    data= ["name", "last name", "age", "birthday", "phone amount"]
    for i in range (len(question)):
            answer[data[i]]=input(question[i])
    return answer
def survey2():
    answer2={}
    question2=["What is your favorite color?", "What state do you live in?", "Do you have any pets?", "Are you a female or male?"]
    data2=["color", "state", "pets","gender"]
    for u in range (len(question2)):
                answer2[data2[u]]=input(question2[u])

    return answer2
import json 

def analyze_data(listtwo):
    num_of_answers=len(listtwo)
    print("Number of responses:"+str(num_of_answers))
   


    
    
def main():
    list1=[]
    list2=[]
    reply3="yes"
    while reply3== "yes":
        
        answer={}
        answer2={}

        print("Hello and thank you for selecting this survey.")
        reply="no"


        while reply=="no":
            
            answer=survey1()
            print("Is this information correct? Type yes or no.")
            print(answer)
            reply=input()




           
        
        print("Do you want to continue this survey? Type 1 to stop, and 2 to continue.")
        reply2=input()
        if reply2 =="1":
                print("Thank you for your time.")
        else:
            answer2=survey2()
            list2.append(answer2)


                
        list1.append(answer)
        print("Do you want to keep on collecting responses?")
        reply3=input()
        
            
    print(list1)
    print(list2)

    listtwo=[]
    listone=[]
    with open ("data.json", 'r') as data:
        listone=json.load(data)
        data.close()
       
    with open ("data.json",'w') as data:
        listone.extend(list1)
        json.dump(listone, data)
        data.close()
    
    
    with open ("data.json", 'r') as mdata:
        listtwo=json.load(mdata)
        
    with open ("data.json",'w') as mdata:
        
        listtwo.extend(list2)
        json.dump(listtwo, mdata)

    analyze_data(listtwo)
    


    

main()

