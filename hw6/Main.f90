Program Main
use matrix_multip
Implicit none

real(4)dimension(5,3):: m
real(4),dimension(3,5):: n
real(4),dimension(5,5):: c
real(4),function matrix_multip
integer i,j,k

Open( unit=1 , File = 'M.dat' )
do i=1,5
    read (1,*) m(i,1:3)
enddo

 do i=1,5
      write (*,'(*(f5.2,1X))') m(i,1:3)
 enddo
close(1)
Open( unit=2 , File = 'N.dat' )
do i=1,3
    read (2,*) n(i,1:5)
enddo
 do i=1,3
    write (*,'(*(f4.2,1X))') n(i,1:5)     
enddo

close(2)

c=matrix_multiply(m,n)
print*,c

open(100,file='MN.dat',status='replace')
do i=1,5
write(111,'(*(f9.2))') c(i,1:5)
enddo
close(111)
end
