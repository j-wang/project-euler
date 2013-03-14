# multiples3and5.rb
# Written by James Wang
# Project Euler Problem 1

# Find the sum of all the multiples of 3 or 5 below 1000.

ans = 0
(3..999).each { |x| if x % 3 == 0 or x % 5 == 0 then ans += x end}
puts ans
