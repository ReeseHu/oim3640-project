import sys
# result_list=['a','a','b','a','a','b','b','a','a','b','a','a']
def run(result_list):
    count_of_a=0
    count_of_b=0
    personality: str = ''
    for i in range(0,4):
        if i=="a":
            count_of_a+=1
        else: 
            count_of_b+=1
    if count_of_a > count_of_b:
        personality = personality + 'E '
    else:
        personality = personality + 'I '
    for i in range(4,7):
        if i=="a":
            count_of_a+=1
        else: 
            count_of_b+=1
    if count_of_a > count_of_b:
        personality = personality + 'S '
    else:
        personality = personality + 'N '   
    for i in range(7,10):
        if i=="a":
            count_of_a+=1
        else: 
            count_of_b+=1
    if count_of_a > count_of_b:
        personality = personality + 'T '
    else:
        personality = personality + 'F ' 
    for i in range(10,13):
        if i=="a":
            count_of_a+=1
        else: 
            count_of_b+=1
    if count_of_a > count_of_b:
        personality = personality + 'J '
    else:
        personality = personality + 'P ' 
    return personality
    


def display(personality_type):
    return(f'Your personality type is {personality_type}.')

# personality = run(result_list)
# print(display(personality))

def main():
    personality = run(result_list)
    print(display(personality))

if __name__ == '__main__':
    main()





