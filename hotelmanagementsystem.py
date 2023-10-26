alr=open('allotedrooms.txt','r+')
alr.close()
thee=1
while thee>0:
  usage=str(input("Do you want to checkin or checkout?"))
  if usage=='checkin' or usage=='Checkin':
    class roomsinfo:
      def __init__(self,type,rooms):
        self.type=type
        self.rooms=rooms

    P1=roomsinfo('ac',[101,102,103,104,105])
    p1=roomsinfo('non-ac',[106,107,108,109,110])
    P2=roomsinfo('ac',[201,202,203,204,205])
    p2=roomsinfo('non-ac',[206,207,208,209,210])
    P3=roomsinfo('ac',[301,302,303,304,305])
    p3=roomsinfo('non-ac',[306,307,308,309,310])
    P4=roomsinfo('ac',[401,402,403,404,405])
    p4=roomsinfo('non-ac',[406,407,408,409,410])
    alr=open('allotedrooms.txt','r+')
    alooms=alr.readlines()
    alrooms=[]
    for i in alooms:
      i=i[1:-1]
      l=i.split(',')
      for r in l:
        alrooms.append(int(r))
    print(alrooms)
    def hotel():
      import random
      def bookroom():
        
        n_p=1
        while n_p>0:
          try:
            np=int(input("Tell no of persons:"))
            if np>0 and np<5:
              n_p=0
            elif np>4:
              print("sorry! at max 4 people in a room is possible")
              n_p+=1
          except:
            print('please enter a valid number')
            n_p+=1
        r_t=1
        global al_room 
        while r_t>0:
          rt=input('tell the room type:ac or non-ac:')
          if rt=='ac':
            r_t=0
          elif rt=='non-ac':
            r_t=0
            
          else:
            print('tell either ac or non-ac')
            r_t+=1
        if np==1 and rt=='ac':
          Rooms=P1.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          P1.rooms.remove(al_room)
        elif np==1 and rt=='non-ac':
          Rooms=p1.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          p1.rooms.remove(al_room)
        elif np==2 and rt=='ac':
          Rooms=P2.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          P2.rooms.remove(al_room)
        elif np==2 and rt=='non-ac':
          Rooms=p2.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          p2.rooms.remove(al_room)
        elif np==3 and rt=='ac':
          Rooms=P3.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          P3.rooms.remove(al_room)
        elif np==3 and rt=='non-ac':
          Rooms=p3.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          p3.rooms.remove(al_room)
        elif np==4 and rt=='ac':
          Rooms=P4.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          P4.rooms.remove(al_room)
        elif np==4 and rt=='non-ac':
          Rooms=p4.rooms
          roo=1
          while roo>0:
            al_room=random.choice(Rooms)
            if str(al_room) in alrooms:
              roo+=1
            else:
              roo=0
          p4.rooms.remove(al_room)
        else:
          print("sorry! you do not have that choice")
        
        
       
        
        if bool(Rooms)==True:
          n=1
          while n>0:
            q=input('Do you need room service? answer yes or no: ')
            if q=='yes':
              rs=1
              n=0
            elif q=='no':
              rs=0
              n=0
            else:
              print('please answer either yes or no')
              n+=1
        n_d=1
        while n_d>0:
          try:
            nd=int(input("please tell the no of days of your stay:"))
            if nd>0:
              n_d=0
          except:
            print("please enter a valid integer:")
            n_d+=1
        
        if nd>0:
            if rt=='ac' and rs==1:
              amount=nd*np*100+nd*2000
            elif rt=='non-ac' and rs==1:
              amount=nd*np*100+nd*1000
            elif rt=='ac' and rs==0:
              amount=nd*np*100+nd*1000
            elif rt=='non-ac' and rs==0:
              amount=nd*np*100
        
        
        print('the amount to be paid is:',amount)
        print("your room is:",al_room)
        print("THANK YOU")
        alrooms.append(al_room)
        alr=open('allotedrooms.txt','w+')
        
        alr.write(str(alrooms))
        
        alr.close()
      bookroom()
    hotel()
    
    print(alrooms)
    thee=0
  elif usage=='checkout' or usage=='Checkout':
    alr=open('allotedrooms.txt','r+')
    alooms=alr.readlines()
    alrooms=[]
    for i in alooms:
      i=i[1:-1]
      l=i.split(',')
      for r in l:
        r=r.strip()
        alrooms.append(int(r))
      
    print(alrooms)
    var=1
    while var>0:
      myroom=input("Please enter your room number:")
      if int(myroom) in alrooms:
        
        alrooms.remove(int(myroom))
        alr=open('allotedrooms.txt','w+')

        alr.write(str(alrooms))
        alr.close()
        print("you are checked out succesfully.THANK YOU")
        print('have a nice day')
        var=0
      elif int(myroom) not in alrooms:
        print('Iam afraid your said wrong room number.Please check once')
        var+=1
      else:
        print('please a valid integer')
        var+=1

      thee=0
  else:
    print('please enter either checkin or checkout')
    thee+=1
