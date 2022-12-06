import sys
result_list=['a','a','b','a','a','b','b','a','a','b','a','a']
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

def descrip(personality):
    description = [{'category':"I S T J",'detail':"Quiet, serious, earn success by thoroughness and dependability. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized - their work, their home, their life. Value traditions and loyalty."},{'category':"I S F J",'detail':"Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home."},{'category':"I N F J",'detail':"Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision."},{'category':"I N T J",'detail':"Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance - for themselves and others."},{'category':"I S T P",'detail':"Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency."},{'category':"I S F P", 'detail':"Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts, do not force their opinions or values on others."},{'category':"I N F P",'detail':"Idealistic, loyal to their values and to people who are important to them. Want an external life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened."},{'category':"I N T P",'detail':"Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical."},{'category':"E S T P",'detail':"Flexible and tolerant, they take a pragmatic approach focused on immediate results. Theories and conceptual explanations bore them - they want to act energetically to solve the problem. Focus on the here-and-now, spontaneous, enjoy each moment that they can be active with others. Enjoy material comforts and style. Learn best through doing."},{'category':"E S F P",'detail':"Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work, and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people."},{'category':"E N F P",'detail':"Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency."},{'category':"E N T P",'detail':"Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another."},{'category':"E S T J",'detail':"Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans."},{'category':"E S F J",'detail':"Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-by-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute."},{'category':"E N F J",'detail':"Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership."},{'category':"E N T J",'detail':"Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas."}]
    for i in description:
        result=i['category']
        # print(result)
        if str(result)==str(personality):
            final=i['detail']
            return final


# def display(personality_type):
#     return(f'Your personality type is {personality_type}.')

# personality = run(result_list)
# print(display(personality))

def main():
    personality = run(result_list).strip()
    print(personality)
    print(descrip(personality))

if __name__ == '__main__':
    main()





