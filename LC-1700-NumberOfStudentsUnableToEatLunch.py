# LeetCode Problem: 1700. Number of Students Unable to Eat Lunch
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0 
        
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0  
            else:
                students.append(students.pop(0))  
                rotations += 1
            
            
            if rotations == len(students):
                break
        
        return len(students)