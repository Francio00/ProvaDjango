var today=new Date();
var hourNow=today.getHours();
var greeting;

if( hourNow >= 18 )
{greeting="Good Evening!";}
else if( hourNow >= 14 )
{greeting="Good Afternoon!";}
else if( hourNow >=6 )
{greeting="Good Morning!";}
else if (hourNow>=0)
{greeting="Good Night!";}

document.write("<h3>"+greeting+"</h3>");
