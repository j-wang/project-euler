# fibonacci.rb
# Written by James Wang
# Project Euler Problem 2

# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.
 
class EvenFib
  include Enumerable
  def initialize (max)
    @max = max
  end
  def each
    x = 2
    n = 7
    while x < @max
        yield x
        n += 3
        x = (((1+Math.sqrt(5))/2)**n/((1+Math.sqrt(5))/2+2)).to_i
    end
  end
end

puts EvenFib.new(4000000).inject { |sum, x| sum + x }
