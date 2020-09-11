.text
.global f

f:
	mul r0, r3, r0
	mul r0, r3, r0
	mul r1, r3, r1
	add r0, r1, r0
	add r0, r2, r0
	bx lr

