int singleNumber(int* nums, int numsSize){
int a = nums[0];
for(int i=1;i<numsSize;i++){
    a = a^nums[i];
    printf("%d\n",a);
}
return a;
}
