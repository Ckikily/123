program Solar_elevation_angle

    use Declination_angle
    use Solar_hour_angle
    
    implicit none
    real                 :: pi
    real :: d, h, local, SEA, lat,angle
    integer,dimension(12) :: months_num
    integer :: mon,day,year

    pi        =  3.14
    months_num      = (/31,28,31,30,31,30,31,31,30,31,30,31/)
    

    year = 2021
    mon  = 12
    day  = 31

  
      d = 366-sum(months_num(mon:))+day
    
    print*,'DAY_num: ', d 

    local = 10.53 
  
    Declination=d+LST/24
    call Declination_angle(Declination,angle)
    call solar_hour_angle(local,h)
    
    if (angle < 0) then
        angle=-angle
      endif


    lat = 22.54

    SEA = 180-asin(sin(lat*pi/360)*sin(angle*pi/360)+cos(lat*pi/360)*cos(angle*pi/360)*cos(h*pi/360))*360/pi
    
    print*,'SEA: ', SEA



    end
