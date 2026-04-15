from plates import is_valid 

def test_is_valid():
    assert is_valid("AA11") == True
    assert is_valid("1AAA") == False
    assert is_valid("AAA111") == True  
    assert is_valid("AA") == True 
    assert is_valid("AA1A") == False        
    assert is_valid("AA01") == False    