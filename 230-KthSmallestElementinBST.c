/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int arr[10000];
 int ct=0;
 void inorder(struct TreeNode* root){
  if (root == NULL)
  return;

  inorder(root->left);

  arr[ct]=root->val;
  ct++;

  inorder(root->right);

}
int kthSmallest(struct TreeNode* root, int k){
    inorder(root);


int sol = arr[k-1];
for(int i=0;i<10000;i++)
arr[i]=0;
ct=0;

    return(sol);
}
