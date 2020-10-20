#include <iostream>
using namespace std;

int main() {
	
	int t;
	cin>>t;
	int i;
	for(i=0;i<t;i++)
	{
	    int n,k;
	    cin>>n>>k;
	    int d;
	    int j;
	    string s="";
	    for(j=0;j<n;j++)
	    {
	        cin>>d;
	        if(d%k==0)
	        {
	            s+="1";
	        }
	        else
	        {
	            s+="0";
	        }
	    }
	    cout<<s<<endl;
	  
	}
	return 0;
}
