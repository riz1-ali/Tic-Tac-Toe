#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<ll,ll> pll;
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define gcd(a,b) __gcd(a,b)
#define lpr(i,s,e) for(ll i=s;i>=e;i--)
#define lpi(i,s,e) for(ll i=s;i<=e;i++)
#define lp(n) for(ll i=0;i<n;i++)
string board[3];
char maxi,mini;
void set_board()
{
	lp(3)
		lpi(j,0,2)
			board[i]+='-';
}
void print_board()
{
	cout<<"  ";
	lp(3)
		cout<<i+1<<" ";
	cout<<endl;
	lp(3)
	{
		cout<<i+1<<" ";
		lpi(j,0,2)
			cout<<board[i][j]<<" ";
		cout<<endl;
	}
}

bool finish_moves()
{
	lp(3)
		lpi(j,0,2)
			if(board[i][j]=='-')
				return 0;
	return 1;
}
bool check_win(char c)
{
	string s="";
	string t="";
	lp(3)
		s+=c;
	lp(3)
		if(board[i]==s)
			return 1;
	lp(3)
	{
		t="";
		lpi(j,0,2)
			t+=board[j][i];
		if(t==s)
			return 1;	
	}
	t="";
	lp(3)
		t+=board[i][i];
	if(t==s)
		return 1;
	t="";
	lp(3)
		t+=board[i][2-i];
	if(t==s)
		return 1;
	return 0;
}
int minimax(int depth,char move)
{
	if(check_win(maxi))
		return 10-depth;
	else if(check_win(mini))
		return depth-10;
	else if(finish_moves())
		return 0;
	int best,f=0;
	char x,y;
	if(move==maxi)
		f=1,best=-20000,x=mini,y=maxi;
	else
		best=20000,x=maxi,y=mini;
	lp(3)
		lpi(j,0,2)
			if(board[i][j]=='-')
			{
				board[i][j]=y;
				if(f)
					best=max(best,minimax(depth+1,x));
				else
					best=min(best,minimax(depth+1,x));
				board[i][j]='-';
			}
	return best;
}
void make_move()
{
	int best=-200,x,y;
	lp(3)
	{
		lpi(j,0,2)
		{
			if(board[i][j]=='-')
			{
				board[i][j]=maxi;
				int be2=minimax(0,mini);
				if(be2>best)
				{
					best=be2;
					x=i,y=j;
				}
				board[i][j]='-';
			}
		}
	}
	board[x][y]=maxi;
}
int main()
{
	cout<<"Welcome! Let's Play Tic Tac Toe\n";
	set_board();
	char o;
	bool turn=1;
	while(1)
	{
		cout<<"Want to go first?(Enter Y/N) ";
		cin>>o;
		if(o=='Y')
		{
			cout<<"You have the first move\n";
			maxi='O';
			mini='X';
			break;
		}
		else if(o=='N')
		{	
			cout<<"I got the first move\n";
			turn=!turn;
			maxi='X';
			mini='O';
			break;
		}
		else
			cout<<"Enter Y/N only!\n";
	}
	int x,y;
	while(1)
	{
		print_board();
		if(turn)
		{
			cout<<"Enter cell row and cell column ";
			cin>>x>>y;
			x--,y--;
			if(board[x][y]!='-')
				cout<<"There's a "<<board[x][y]<<" there already, choose again\n";
			else
			{
				board[x][y]=mini;
				turn=!turn;
			}
		}
		else
		{
			cout<<"My turn\n";
			make_move();
			turn=!turn;
		}
		if(check_win(maxi))
		{
			print_board();
			cout<<"I won\n";
			break;
		}
		else if(check_win(mini))
		{
			print_board();
			cout<<"Well Played\n";
			break;
		}
		else if(finish_moves())
		{
			print_board();
			cout<<"Draw\n";
			break;
		}
	}
	return 0;
}