/**
 * pid != 0 
 * i = 1 (1)  ==> pid == 0
 *           i = 0 (1.1)
 * 
 * parent ==> fork() ==>child ==> exec() ==> exit()
 *            parent() ==> wait()<============= status
 * 
 * /
 * 
 * */