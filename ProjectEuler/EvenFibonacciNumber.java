/**
 * Finds the sum of the even-terms in the Fibonacci sequence whose values do not exceed four million.
 */
class EvenFibonacciNumber{

    private static int SumOfEvenFibonacciNumber(int max){
        int sum, temp;
        int adder1 = 0, adder2 = 1;

        sum = temp = 0;

        while(temp <= max){

            temp = adder1 + adder2;
            if(temp%2==0){
                sum += temp;
            }
            adder1 = adder2;
            adder2 = temp;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(SumOfEvenFibonacciNumber(4000000));
    }
}