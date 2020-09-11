.text

.global summ
summ:

forStart:
	ldrb r3, [r2], #4
	add r0, r3
	sub r1, r1, #1
	cmp r1, #0
	bgt forStart
	mov r1, r0
	bx lr

