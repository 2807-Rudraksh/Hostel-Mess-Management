import random

plans=(("Standard", 2000), ("Premium", 3000))
ava_addons={"Milk","Snacks","Juice"}

student_rec={}

def add_student():
    sid=input("Enter student ID: ")
    name=input("Enter student name: ")

    print("Available Plans:")
    for i,(p,c) in enumerate(plans, 1):
        print(f"{i}.{p} - {c}")
    choice=int(input("Choose plan (1/2): "))
    plan, cost = plans[choice - 1]

    print(f"Available Add-ons: {' , '.join(ava_addons)}")
    addons=input("Enter add-ons (comma separated, or leave blank): ").title().split(",")
    addons=[a.strip() for a in addons if a.strip() and a.strip() in ava_addons]

    student_rec[sid]={"name": name, "plan": plan, "addons": addons, "paid": False}
    print(f"Student {name} added successfully!")

def view_students():
    if not student_rec:
        print("No records found.")
        return
    print("---All Student Records---")
    for sid, info in student_rec.items():
        print(f"ID:{sid} | Name:{info['name']} | Plan:{info['plan']} | Add-ons:{info['addons']} | Paid:{info['paid']}")

def modify_student():
    sid=input("Enter student ID to modify: ")
    if sid not in student_rec:
        print("Student not found.")
        return
    print("1. Change Plan  2. Add/Remove Add-ons  3. Mark as Paid")
    ch=input("Enter choice:")
    if ch=="1":
        for i, (p,c) in enumerate(plans, 1):
            print(f"{i}. {p} - {c}")
        choice=int(input("Choose new plan: "))
        student_rec[sid]["plan"]=plans[choice - 1][0]
    elif ch=="2":
        print(f"Available add-ons: {' , '.join(ava_addons)}")
        addons=input("Enter new add-ons (comma separated): ").title().split(",")
        student_rec[sid]["addons"]=[a.strip() for a in addons if a.strip() in ava_addons]
    elif ch=="3":
        student_rec[sid]["paid"]=True
    print("Record updated!")

def delete_student():
    sid=input("Enter student ID to delete: ")
    if sid in student_rec:
        del student_rec[sid]
        print("Record deleted.")
    else:
        print("Student not found.")

def calculate_bill():
    sid=input("Enter student ID to calculate bill: ")
    if sid not in student_rec:
        print("Student not found.")
        return
    info=student_rec[sid]
    plan_cost=next(c for p, c in plans if p==info["plan"])
    addon_cost=len(info["addons"]) * random.randint(100,150)
    total=plan_cost + addon_cost
    print(f"---Bill for {info['name']}---")
    print(f"Plan: {info['plan']} - {plan_cost}")
    print(f"Add-ons: {info['addons']} - {addon_cost}")
    print(f"Total Amount: {total}\n")

def pending_report():
    print("---Pending Payments---")
    pending=[s for s in student_rec.values() if not s["paid"]]
    if not pending:
        print("All payments done!")
    else:
        for s in pending:
            print(f"{s['name']} - Plan: {s['plan']} - Paid: {s['paid']}")

def plan_summary():
    print("---Subscription Plan Summary---")
    summary={}
    for p, _ in plans:
        summary[p]={"count": 0, "revenue": 0}
    for s in student_rec.values():
        for p, c in plans:
            if s["plans"]==p:
                summary[p]["count"] += 1
                summary[p]["revenue"] += c
    for p, data in summary.items():
        print(f"{p}: {data['count']} students, Revenue: {data['revenue']}")
    print()

#----Main Menu----
while True:
    print("=== HOSTEL MESS SUBSCRIPTION & BILLING ===" )
    print("1. Add Student   2. View Student   3. Modify Student   4. Delete Student")
    print("5. Calculate Bill   6. Pending Payments    7. Plan Summary  8. Exit")

    choice=input("Enter your choice: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        modify_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        calculate_bill()
    elif choice=="6":
        pending_report()
    elif choice=="7":
        plan_summary()
    elif choice=="8":
        print("Exiting the program")
        break
    else:
        print("Invalid choice, try again.")


