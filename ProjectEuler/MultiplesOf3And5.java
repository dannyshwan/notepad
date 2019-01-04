/**
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

class MultiplesOf3And5{
    
    public static int SumOf3And5(int number){

        int sum, i;
        sum = i = 0;

        while(i < number){
            if(i%3==0 || i%5==0){sum += i;}
            i++;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(SumOf3And5(1000)); // Should print 233168
    }
}