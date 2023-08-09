# 2582. Pass the Pillow

There are n people standing in a line labeled from 1 to n. The first person </br>
in the line is holding a pillow initially. Every second, the person holding </br>
the pillow passes it to the next person standing in the line. Once the pillow </br>
reaches the end of the line, the direction changes, and people continue passing </br>
the pillow in the opposite direction. </br>

For example, once the pillow reaches the nth person they pass it to the n - </br>
1th person, then to the n - 2th person and so on. </br>
Given the two positive integers n and time, return the index of the person  </br>
holding the pillow after time seconds. </br>

## Example 1:

Input: n = 4, time = 5 </br>
Output: 2 v
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2. </br>
Afer five seconds, the pillow is given to the 2nd person. </br>

## Example 2:

Input: n = 3, time = 2 </br> 
Output: 3 </br>
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3. </br>
Afer two seconds, the pillow is given to the 3rd person. </br>

## Constraints:

2 <= n <= 1000 </br>
1 <= time <= 1000 </br>
