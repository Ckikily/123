  real(4) function matrix_multiply(m,n)
  real(4),dimension(5,3):: m
  real(4),dimension(3,5):: n
  real(4),dimension(5,5):: c
  integer i
do i=1,5
  c(1,i)=dot_product(n(i:),m(:1))
enddo
do i=1,5
    c(2,i)=dot_product(n(i:),m(:2))
enddo
do i=1,5
  c(3,i)=dot_product(n(i:),m(:3))
enddo
do i=1,5
  c(4,i)=dot_product(n(i:),m(:4))
enddo
do i=1,5
  c(5,i)=dot_product(n(i:),m(:5))
enddo
end function matrix_multiply
   
