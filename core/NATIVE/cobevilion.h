#include <stdio.h> //Standard headers
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <libxml/xmlmemory.h> //libxml2 headers
#include <libxml/parser.h>
#include <libxml/parserInternals.h>
#include <libxml/tree.h>
#include <libxml/threads.h>
#include <pthread.h>	//POSIX threads

char default_ABC[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

const char CMD_DETECT[] = "file -i -b %s"; //this command return what is the file mime type

const char* TYPE[] = {"rar",		"7z",		"zip", ""}; //the last "" signing this is end of the list
const char* MIME[] = {"application/x-rar", "application/octet-stream", "application/x-zip", ""};
const char* CMD[] = {"unrar t -y -p%s %s 2>&1", "7z t -y -p%s %s 2>&1", "unzip -P%s -t %s 2>&1", ""};

#define PWD_LEN 100
