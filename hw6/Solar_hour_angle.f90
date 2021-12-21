module Solar_hour_angle

    implicit none
    
        contains
    
            subroutine solar_hour_angle(local,h)
            real, intent(in)    :: local
            real, intent(out)   :: h
            
            h = 15*(local-12)
            print*, 'solar_hour_angle is : ', h
            
            end subroutine solar_hour_angle
    
    end module Solar_hour_angle
    

