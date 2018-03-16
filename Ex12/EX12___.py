import re
text="""0000zzzVVVzzzWWWzzzVVV---_WWW......._-_--.
WWWWWWzzzWWW[a(>RWWW$0000aaaazzz$zzz$>VVVR0000WWW@
0000aaWWWVVV0000$aWWWx[[[zzzzzz.'aa-=-'aWWWVVV`.
WWW[[aWWWxzzzzzzx00000000aa.'VVVzzzVVVVVVzzzzzzWWWVVVzzzWWWzzzVVVVVV)
0000VVV0000_xVVV[xzzzWWWa.'00000000VVV0000[aazzz_.)0000zzz0000$
0000a$WWWoWWW[WWWozzzaazzz[0000[zzz_.-'VVVxWWW0000.'
0000zzzRa0000a0000zzzzzz0000VVVWWWa_.-'VVVazzzax0000.'*2
VVVVVVVVVR______.-'xxVVVWWW0000WWW.'.'zzzR*>
VVVWWW0000a@2zzzVVV@VVV>zzzx$VVVzzzWWW.'.'WWW_WWW>*2
VVV[0000[zzz`[VVVa@>$$zzza.'.'_a_[_>*>
WWW0000VVVVVVVVVWWW.aa.$x[.'.'WWW2zzz_0000_WWW@*>
[0000[zzzzzzWWWR`-2R_$zzzx0000VVVaWWW@a_[_a@*@
00000000[zzz[WWWa`$'@__x[0000WWW0000VVVzzz@VVV_[_[R*@
WWWa[zzzaVVV$^2azzzzzzzzz[0000VVVVVVVVVWWWVVVaR0000_a_aR*
zzzWWWzzzzzzWWW'zzzWWW`[zzz[zzzaVVVa0000VVVWWWWWWzzzaR0000_[_a@
ASHa(+VK)zzzWWWVVV[WWW0000[[[00000000zzzWWWa@_"""

clear=text
#here is one substitution that you will need
#but you have to write the other ones according to the spec
clear = re.sub(r">|2", r"|", clear)  #hint: ">","2" must turn into |
clear = re.sub(r"a|VVV|zzz|0000|\[|WWW", r" ", clear)
clear = re.sub(r"x|\$", r"/", clear)
clear = re.sub(r"@|R", r"\\", clear)

print(clear)
