# 1. What is a list in Python?
my_list = ["Kaladi", 22, True]
print("Q1:", my_list)

# 2. Valid list declaration
student = ["Subhan", 15, "Karachi"]
print("Q2:", student)

# 3. marks[1:4]
marks = [87, 64, 33, 95, 75]
print("Q3:", marks[1:4])  # [64, 33, 95]

# 4. marks[:4] = elements from 0 to 3
print("Q4:", marks[:4])  # [87, 64, 33, 95]

# 5. marks[2:] = elements from index 2 to end
print("Q5:", marks[2:])  # [33, 95, 75]

# 6. append() adds at the end
my_list2 = [1, 2, 3]
my_list2.append(4)
print("Q6:", my_list2)

# 7. list.append(4) on [2, 1, 3]
lst = [2, 1, 3]
lst.append(4)
print("Q7:", lst)  # [2, 1, 3, 4]

# 8. sort() sorts ascending
lst2 = [3, 1, 2]
lst2.sort()
print("Q8:", lst2)  # [1, 2, 3]

# 9. list.sort() on [2, 1, 3]
lst3 = [2, 1, 3]
lst3.sort()
print("Q9:", lst3)  # [1, 2, 3]

# 10. sort(reverse=True) = descending
lst4 = [2, 1, 3]
lst4.sort(reverse=True)
print("Q10:", lst4)  # [3, 2, 1]

# 11. reverse() just reverses current order
lst5 = [2, 1, 3]
lst5.reverse()
print("Q11:", lst5)  # [3, 1, 2]

# 12. insert() adds at specific index
lst6 = [2, 1, 3]
lst6.insert(1, 5)
print("Q12:", lst6)  # [2, 5, 1, 3]

# 13. insert(1, 5)
lst7 = [2, 1, 3]
lst7.insert(1, 5)
print("Q13:", lst7)  # [2, 5, 1, 3]

# 14. remove() removes first occurrence
lst8 = [2, 1, 3, 1]
lst8.remove(1)
print("Q14:", lst8)  # [2, 3, 1]

# 15. list.remove(1)
lst9 = [2, 1, 3, 1]
lst9.remove(1)
print("Q15:", lst9)  # [2, 3, 1]

# 16. pop(index) removes & returns value
lst10 = [2, 1, 3, 1]
popped = lst10.pop(1)
print("Q16:", popped, lst10)  # 1, [2, 3, 1]

# 17. list.pop(1)
lst11 = [2, 1, 3, 1]
lst11.pop(1)
print("Q17:", lst11)  # [2, 3, 1]

# 18. tuple = immutable
my_tuple = (1, 2, "Subhan")
print("Q18:", my_tuple)

# 19. valid tuple
tup = (87, 64, 33)
print("Q19:", tup)

# 20. index() in tuple
tup2 = (10, 20, 10, 30)
print("Q20:", tup2.index(10))  # 0
