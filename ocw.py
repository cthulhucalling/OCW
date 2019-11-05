#!/usr/bin/python

rifle=raw_input("Enter rifle make: ")
caliber=raw_input("Enter caliber: ")
bullet=raw_input("Enter bullet make: ")
bullet_weight=raw_input("Enter bullet weight in grains: ")
powder=raw_input("Enter powder: ")
max_powder_weight=float(raw_input("Enter max powder weight in grains: "))
file=open("OCW for "+str(rifle)+" "+str(caliber),'w')

file.write("Optimal Charge Weight for %s %s shooting %s %sgr bullets" %(rifle,caliber,bullet,bullet_weight)+"\n")
file.write("Powder: %s" %(powder)+"\n")
file.write("\n")

file.write("Load one round for each of the following charge weights: %s, %s, %s" %(round(max_powder_weight*.9,1),round(max_powder_weight*.92,1),round(max_powder_weight*.94,1))+"\n")
file.write("These rounds are your sighters to foul the barrel and verify that you're reasonably on target. Inspect each for signs of overpressure."+"\n")

counter=1
round_one_weight=round(max_powder_weight*.96,1)
file.write("Group %s: Load three rounds with %sgr of %s" %(counter,round_one_weight,powder)+"\n")
new_powder_weight=round_one_weight
while new_powder_weight < max_powder_weight:
        new_powder_weight=round(new_powder_weight*1.007,1)
        counter=counter+1
        file.write("Group %s: Load three rounds with %sgr of %s" %(counter,new_powder_weight,powder)+"\n")

file.close()
file=open("OCW for "+str(rifle)+" "+str(caliber),'r')
print file.read()
