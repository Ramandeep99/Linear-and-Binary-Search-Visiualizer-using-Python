from time import sleep
from os import name,system

def clearscreen():
	if name=='nt':
		system('cls')
	else:
		system('clear')

print()
print('				Press 1 FOR LINEAR SEARCH VISUALISER ')
print()
print('				Press 2 for BINARY SEARCH VISUALISER ')
print()
try:
	n=int(input('Enter your choice : '))
	print()
	if n==1:
		print()
		print(' 				---LINEAR SEARCH VISUALISER--- ')
		try:
			# print('ENTER THE -ARRAY USING SPACE : ')
			l=list(map(int,input("ENTER THE ARRAY USING SPACE : ").split()))
			print()
			# print('Enter element you want to search : ')
			x=int(input('Enter element you want to search : '))
			print()
			ans=0
			for i in range(len(l)):
				print(*l)
				s=[]
				for j in range(i):
					s.append(str(l[j]))
				t=''.join(s)
				print(" "*len(t)+' '*i ,"^",sep='')
				print(' '*len(t)+' '*i ,x,sep='')

				if l[i]==x:
					index=i
					ans=1
					break
				else:
					sleep(1)
					clearscreen()
			if ans==1:
				print('Element found at index',index)
				print()
			else:
				print('Element not found in entered array')
				print()
		except:
			print('Enter array according to given instructions')
			print()

	elif n==2:
		print()
		print('				---BINARY SEARCH VISUALISER---')
		print()
		try:
			# print('ENTER ARRAY USING SPACE IN SORTED ORDER')
			l=list(map(int,input('ENTER ARRAY USING SPACE IN SORTED ORDER : ').split()))
			print()
			if l!=sorted(l):
				print('Entered array is not in sorted manner ')
				print()
				ans=input('Enter "yes" if want to search in same array by sorting it,else enter "no" : ')
				if ans=='no':
					print()
					# break
				elif ans=='yes':
					# print('Enter Element you want to search')
					l.sort()
					x=int(input('Enter Element you want to search : '))
					print()
					start=0
					end=len(l)-1
					flag=0
					while start<=end:
						# print(len(str(x)))
						mid=(start+end)//2
						print(*l)
						p=[]
						for i in range(mid):
							p.append(str(l[i]))
						k=''.join(p)
						print(" "*len(k)+' '*mid  ,"^",sep='')
						print(' '*len(k)+' '*mid,x,sep='')

						if l[mid]==x:
							index=mid
							flag=1
							break
						elif l[mid]<x:
							start=mid+1
							sleep(3)
							clearscreen()
						else:
							end=mid-1
							sleep(1)
							clearscreen()
					if flag==1:
						print('Entered element found at index',index)
						print()
					else:
						print('Entered element not found in entered array')
						print()
			else:
				print()
				x=int(input('Enter Element you want to search : '))
				print()
				start=0
				end=len(l)-1
				flag=0
				while start<=end:
					# print(len(str(x)))
					mid=(start+end)//2
					print(*l)
					p=[]
					for i in range(mid):
						p.append(str(l[i]))
					k=''.join(p)
					print(" "*len(k)+' '*mid  ,"^",sep='')
					print(' '*len(k)+' '*mid,x,sep='')

					if l[mid]==x:
						index=mid
						flag=1
						break
					elif l[mid]<x:
						start=mid+1
						sleep(3)
						clearscreen()
					else:
						end=mid-1
						sleep(3)
						clearscreen()
				if flag==1:
					print('Entered element found at index',index)
					print()
				else:
					print('Entered element not found in entered array')
					print()
		except:
			print('Enter according to given instructions')
	else:
		print('Enter valid key')
except:
	print('Enter according to given instructions')

k=input("Press enter to exit")
system('cls')


