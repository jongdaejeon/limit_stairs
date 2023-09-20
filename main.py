M = [
    '11111',
    '00000',
    '00001',
    '00010',
    '00100',
    '01000',
    '10000',
    '01000',
    '00100',
    '00010',
    '00100',
    '00010',
    '10000',
    '01000',
    '00100',
    '01000',
    '10000',
]
height = len(M) - 5
flag_a = False 
flag_b = False
def on_forever():
    global height, flag_a, flag_b
    if height ==0:
        return
    a = M[height:height+5]    
    for y in range(5):
        for x in range(5):
            led.plot_brightness(x,y, int(a[y][x]) *  255)
        ib = a[4].index_of('1')
        it = a[3].index_of('1')

        up = False
        fail = False

    # check botton statue
    if flag_a:
       flag_a = False
       if it < ib:
           up = True
       else:
           fail = True

    if flag_b:
        flag_b = False
        if it > ib:
            up = True
        else:
            fail = True
    if up:
        height -= 1
    if fail:
        soundExpression.sad.play_until_done()
        height = len(M) - 5
    #basic.pause(100)

basic.forever(on_forever)

def on_button_pressed_a():
    global flag_a 
    flag_a =True 
    
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global flag_b
    flag_b =True
    
input.on_button_pressed(Button.B, on_button_pressed_b)
# a = M[height:height+5]
# for y in range(5):
#     for x in range(5):
#         led.plot_brightness(x,y, int(a[y][x]) *  255)
# basic.show_number(height)

# def on_button_pressed_a():
#     global height, M
#     if height == 0:
#         return
#     a = M[height:height+5]
#     ib = a[4].index_of('1')
#     it = a[3].index_of('1')
#     if ib > it:
#         height -= 1
#     else:
#         heihgt = len(M)-5
#         music.string_playable("", 120)

#     a = M[height:height+5]
#     for y in range(5):
#         for x in range(5):
#             led.plot_brightness(x,y, int(a[y][x]) *  255)
# def on_button_pressed_b():
#     global height, M
#     if height == 0:
#         return
#     a = M[height:height+5]
#     ib = a[4].index_of('1')
#     it = a[3].index_of('1')
#     if ib < it:
#         height -= 1
#     else:
#         music.built_in_playable_melody(Melodies.DADADADUM)
#         heihgt = height

#     a = M[height:height+5]
#     for y in range(5):
#         for x in range(5):
#             led.plot_brightness(x,y, int(a[y][x]) *  255)


# input.button_is_pressed(Button.A,on_button_pressed_a)
# input.button_is_pressed(Button.B,on_button_pressed_b)

