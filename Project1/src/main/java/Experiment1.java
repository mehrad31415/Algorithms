
/**
 *
 * @author mehradhq
 */
import java.util.Arrays;
import java.util.Random;

public class Experiment1 {

    public static void main(String[] args) {
        // these are the constants of the experiment.
        // numArrays is the number of arrays created which in this case is 500.
        // numRuns is the number of executions on each array which in this case is 10.
        // minSize is the minimum array size which is 5.
        // the step is 5 which will be added to the minSize on each iteration. 
        // for 500 iterations, the maximum array size will become 2500.
        int numArrays       = 500;
        int numRuns         = 10;
        int minSize         = 5;
        int step            = 5;

        // the size array is the array containing the size of each of the arrays.
        // selection sort contains the mean time of the 100 executions of each of the arrays.
        // merge sort contains the mean time of the 100 executions of each of the arrays.
        int [] size          = new int[numArrays];
        long[] selectionSort = new long[numArrays];
        long[] mergeSort     = new long[numArrays];

        Random random = new Random();
        
        // 1000 iterations for creating 1000 different arrays.
        for (int i = 0; i < numArrays; i++) {
            // the varying array size from 10 to 10,000
            int arraySize = minSize + i * step;
            size[i] = arraySize;
            
            // we create a random array on each iteration.
            int[] randomArray = new int[arraySize];
            for (int j = 0; j < arraySize; j++) {
                // generating any random number without bounds.
                int r = random.nextInt();
                // the loop ensures non duplicate elements
                while (contains(randomArray, r)){
                    r = random.nextInt();
                }
                randomArray[j] = r;
            }

            long selectionSortTime = 0;
            long mergeSortTime     = 0;
            
            // for each array we run the algorithms 100 times.
            for (int j = 0; j < numRuns; j++) {
                // we create a copy of the array because if the array is not copied and sorted then we will have sorted arrays on the next execution.
                // note that there is no need for a deep copy because the array consists of integers.
                int[] selectionSortArray = Arrays.copyOf(randomArray, arraySize);
                int[] mergeSortArray = Arrays.copyOf(randomArray, arraySize);

                // we calculate the running time of the algorithm of the selection sort on the array.
                long selectionSortStartTime = System.nanoTime();
                selectionSort(selectionSortArray);
                long selectionSortEndTime = System.nanoTime();
                // we calculate the running time of the algorithm of the merge sort on the array.
                long mergeSortStartTime = System.nanoTime();
                mergeSort(mergeSortArray,0,mergeSortArray.length-1);
                long mergeSortEndTime = System.nanoTime();

                // we calculate the cumulatives.
                selectionSortTime += (selectionSortEndTime - selectionSortStartTime);
                mergeSortTime     += (mergeSortEndTime - mergeSortStartTime);
            }

            // we calculate the mean of the time. Note the data type is long because the type is expressed with a lot of decimals.
            long meanSelectionSortTime = selectionSortTime / numRuns;
            long meanMergeSortTime     = mergeSortTime / numRuns;

            selectionSort[i] = meanSelectionSortTime;
            mergeSort[i]     = meanMergeSortTime;
        }
        System.out.println(Arrays.toString(selectionSort));
        System.out.println(Arrays.toString(mergeSort));
    }

    // selection sort algorithm
    public static void selectionSort(int[] arr) {
        int temp;
        for (int i = 0; i < arr.length; i++) {
            temp = arr[i];
            arr[i] = arr[minimum(i, arr)];
            arr[minimum(i, arr)] = temp;

        }
    }
    // returns the index of the minimum element of the array starting from 'index'.
    public static int minimum(int index, int[] arr) {
        int min = arr[index];
        int ind = index;
        for (int i = index; i < arr.length; i++) {
            // ensure stability.
            if (arr[i] < min) {
                ind = i;
                min = arr[i];
            }
        }
        return ind;
    }
    // checks if an array contains an element. It is the equivalent of contains for ArrayList.
    public static boolean contains(int[] arr, int target) {
    for (int element : arr) {
        if (element == target) {
            return true;
        }
    }
    return false;
}
    
    // All of the following lines of code were taken from geeksforgeeks. 
    // https://www.geeksforgeeks.org/java-program-for-merge-sort/
    public static void merge(int arr[], int l, int m, int r) {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;

        // Create temp arrays
        int L[] = new int[n1];
        int R[] = new int[n2];

        // Copy data to temp arrays
        for (int i = 0; i < n1; ++i) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j];
        }

        // Merge the temp arrays
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;

        // Initial index of merged subarray array
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of L[] if any
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        // Copy remaining elements of R[] if any
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    public static void mergeSort(int arr[], int l, int r) {
        if (l < r) {
            // Find the middle point
            int m = (l + r) / 2;

            // Sort first and second halves
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }
    
}
