/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int arr[100000];
 int ct=0;
void inorder(struct TreeNode* root){
  if (root == NULL)
  return;

  inorder(root->left);

  arr[ct]=root->val;
  ct++;

  inorder(root->right);

}
int getMinimumDifference(struct TreeNode* root){

inorder(root);
int dif;
int sol = 999999;
for(int i=0;i<ct-1;i++){
  dif = abs(arr[i]-arr[i+1]);
  printf("dif %d\n",dif);
  if (dif<sol)
    sol=dif;
}
for(int i=0;i<100000;i++)
arr[i]=0;
ct=0;
return(sol);
}
