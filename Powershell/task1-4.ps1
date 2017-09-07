#Mandatory Powershell assignment, 1-4.

#The Encrypted string says 'Keyboard not found. Press F1 to continue'

function decrypt($char){

    $number = [int][char]$char
    $number = $number - 1;

    return [char]$number
}

function encrypt($char){

    $number = [int][char]$char
    $number = $number +1;

    return [char]$number
}

function decryption($string){
    
    $string_list = $string.ToCharArray()
    $result_list = foreach($char in $string_list){
        decrypt($char) 

    }

    $result = [string]$result_list
    return $result
}

function encryption($string){
    
    $string_list = $string.ToCharArray()
    $result_list = foreach($char in $string_list){
        encrypt($char)
    }

    return [string]$result_list
}

decryption -string 'Lfzcpbse!opu!gpvoe/!Qsftt!G2!up!dpoujovf'

encryption -string 'Keyboard not found. Press F1 to continue'