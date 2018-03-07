##
## EPITECH PROJECT, 2017
## project name
## File description:
## Makefile for project name
##

SRC		=	src/main.c

OBJ		=	$(SRC:.c=.o)

CPPFLAGS	+=	-I include

CFLAGS		+=	-Wall -Wextra -g

LDFLAGS		+=	-Llib/ -lmy -lgraph

NAME		=	

all	:	$(NAME)

$(NAME)	:	$(OBJ)
		make lib
		gcc -o $(NAME) $(OBJ) $(LDFLAGS)

lib	:	lib/my/Makefile	lib/graph/Makefile
		make -C lib/my
		make -C lib/graph

tests_run:
		make lib
		make -C tests/
		./tests/units

clean	:
		rm -f $(OBJ)
		rm -f *.gc*
		make clean -C lib/my
		make clean -C lib/graph
		make clean -C tests

fclean	:	clean
		rm -f $(NAME)
		make fclean -C lib/my
		make fclean -C lib/graph
		make fclean -C tests

re	:	fclean	all

.PHONY	:	all lib tests_run clean fclean re
