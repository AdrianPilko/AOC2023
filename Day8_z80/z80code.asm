
;;; memory model:
;;; 0x0000 to 7fff      - ROM
;;; 0x8000 to to 0xffff - RAM
;;; 
#define ROM_SIZE $7fff
#define SIZE_OF_SYSTEM_VARIABLES $0004
#define STACK_BOTTOM $ffff
#define RAM_START $8000  

;; port definitions
#define lcdRegisterSelectCommand $00   ; all zero address including line 0 which is connected to the LCD  ReadSelect (RS) pin 
#define lcdRegisterSelectData $01      ; all zero address except line 0 which is connected to the LCD  ReadSelect (RS) pin 
#define keypadInOutPort $20             ; A6 high the rest low

    .org $0
    
    ld  sp , STACK_BOTTOM 
    
    call initialiseLCD
    call setLCDRow2

    ld hl, $0000     ; result starts off as 0 and is preincremented in the loop, but the adjusted later
    ld (result), hl    
    ld hl, inputDataLR_AsNum
    ld (currentPosInLR), hl
    ld hl, inputDataAAAPos
        
mainLoop:     
    ;; delay loop with heart beat to see what's happening on lcd
    
    call displayStar
    call delaySome
    call displayBlankWhereeStarWas
    call delaySome
    call displayBlankWhereLWas
    call displayBlankWhereRWas
;    push hl 
;    ld hl, (currentPosInLR)
;    call hexprint16_onRight
;    pop hl
        
    ;;jp mainLoop
    push hl 
    ld hl, currentPosInLR
    ld a, (hl)    
    call hexprint16_onRight
    pop hl
    cp 0
    jp z, goLeft
    ;; else go right
goRight:
    call displayR
    push hl     ; preserve hl 
    ;adjust the LR index
    ld hl, (currentPosInLR)
    inc hl 
    ld (currentPosInLR), hl
    
    ld bc, inputDataMAX_LR    
    sbc hl, bc    ; hl still has currentPosInLR    
    jp nz, goRightCarryOn   ; 
    
    ld hl, inputDataLR_AsNum ; reset LR to start
    ld (currentPosInLR), hl
goRightCarryOn:        
    ; increment result
    ld hl, (result)
    inc hl
    ld (result), hl
    pop hl
    
    inc hl   ; this gets us to the right index pos
    inc hl   ; this gets us to the right index pos    
    push hl  ; get hl in bc
    pop de
    dec hl   ; restore hl to start of "row"
    dec hl   ; restore hl to start of "row"    
    add hl, de  ;; gets hl to the next "row" start

    
    push hl  ; print result as we go (mainly for debug!)
    call setLCDRow2
    ld hl, (result)
    call hexprint16
    pop hl 

    push hl
    ld bc,(inputDataZZZPos)  ; check if we are at ZZZ
    ; Compare HL and BC to see if we are at the ZZZ memory location
    sbc hl, bc        
    pop hl   ; restore hl for next loop but flags not affected
    jp nz, mainLoop   ; carry on 
    jp displayResult       
goLeft:
    call displayL
    push hl     ; preserve hl 
    ;adjust the LR index
    ld hl, (currentPosInLR)
    inc hl 
    ld (currentPosInLR), hl
    
    ld bc, inputDataMAX_LR    
    sbc hl, bc    ; hl still has currentPosInLR    
    jp nz, goLeftCarryOn   ; 
    
    ld hl, inputDataLR_AsNum ; reset LR to start
    ld (currentPosInLR), hl
goLeftCarryOn:    
    ; increment result
    ld hl, (result)
    inc hl
    ld (result), hl
    pop hl
    
    inc hl   ; this gets us to the left index pos
    
    push hl  ; get hl in bc
    pop de
    dec hl   ; restore hl to start of "row"
    add hl, de  ;; gets hl to the next "row" start
    
    push hl      ; print result as we go (mainly for debug!)
    call setLCDRow2
    ld hl, (result)
    call hexprint16
    pop hl 
    
    push hl
    ld bc,(inputDataZZZPos)  ; check if we are at ZZZ
    ; Compare HL and BC to see if we are at the ZZZ memory location
    sbc hl, bc        
    pop hl   ; restore hl for next loop but flags not affected    
    jp nz, mainLoop   ; carry on 
    
    ;;jp displayResult  don't need to jp as is just next instruction!

displayResult:    
    call setLCDRow2
    ld hl, (result)    
    call hexprint16
        
    halt

delaySome:    
    push bc    ; preserve bc register
    ld b, $ff
waitLoopAfterKeyFound11:    
    push bc
    ld b, $7f
waitLoopAfterKeyFound22:        
    djnz waitLoopAfterKeyFound22
    pop bc
    djnz waitLoopAfterKeyFound11
    
    pop bc
    ret
    
  
initialiseLCD:
    ld hl,InitCommandList
    call waitLCD
loopLCDInitCommands
    ld a, (hl)
    cp $ff
    jp z, outputBootMessage
    out (lcdRegisterSelectCommand), a     ; send command to lcd (assuming lcd control port is at 0x00)
    inc hl
    jp loopLCDInitCommands    
outputBootMessage:
    ld hl, BootMessage
loopLCDBootMessage:         
    call waitLCD 
    ld a, (hl)
    cp $ff
    jp z, initialiseLCD_ret
    out (lcdRegisterSelectData), a
    inc hl
    jp loopLCDBootMessage    
initialiseLCD_ret    
    ret

displayStar
    push af
    call waitLCD
    ld a, $80+$45        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call waitLCD    
    ld a, '*'
    out (lcdRegisterSelectData), a
    pop af    
    ret
displayBlankWhereeStarWas
    push af
    call waitLCD
    ld a, $80+$45        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call waitLCD    
    ld a, ' '
    out (lcdRegisterSelectData), a
    pop af    
    ret
 
displayL
    push af
    call waitLCD
    ld a, $80+$46        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call waitLCD    
    ld a, 'L'
    out (lcdRegisterSelectData), a
    pop af    
    ret
displayR
    push af
    call waitLCD
    ld a, $80+$47        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call waitLCD    
    ld a, 'R'
    out (lcdRegisterSelectData), a
    pop af    
    ret    

displayBlankWhereLWas
    push af
    call waitLCD
    ld a, $80+$46        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call waitLCD    
    ld a, ' '
    out (lcdRegisterSelectData), a
    pop af    
    ret 
displayBlankWhereRWas
    push af
    call waitLCD
    ld a, $80+$47        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call waitLCD    
    ld a, ' '
    out (lcdRegisterSelectData), a
    pop af    
    ret 
  
    
;;; "generic" display code
; self evident, this clears the display
clearDisplay:
    push af
    call waitLCD
	ld a, $01
	ld (lcdRegisterSelectCommand), a
    pop af
	ret 

setLCDRow1:
    call waitLCD
    ld a, $80         ; Set DDRAM address to start of the first row
    out (lcdRegisterSelectCommand), a     ; Send command to LCD         
    ret 

setLCDRow2:
    push af
    call waitLCD
    ld a, $80+ $40        ; Set DDRAM address to start of the second line (0x40)
    out (lcdRegisterSelectCommand), a     ; Send command to LCD         
    pop af
    ret   

moveCursorToPostion:  ;; b store the cursor position 
	call waitLCD
	ld a, $fe
    ld (lcdRegisterSelectCommand), a
	call waitLCD
	ld a, $80      ; start offset into ddram for cursor, if b=0 thats top left
	add a, b
    ld (lcdRegisterSelectCommand), a	
	ret

;;; make sure the lcd isn't busy - by checking the busy flag
waitLCD:    
    push af
waitForLCDLoop:             
    in a,(lcdRegisterSelectCommand)  
    rlca              
    jr c,waitForLCDLoop    
    pop af
    ret 
    
displayCharacter:    ; register a stores tghe character
    call waitLCD
    out (lcdRegisterSelectData), a
    ret 

hexprint16_onRight
    call waitLCD
    ld a, $80+$49        ; Set DDRAM address to start line 2 plus 5
    out (lcdRegisterSelectCommand), a     ; Send command to LCD    
    call hexprint16
    
    ret

    
hexprint16  ; print one 2byte number stored in location $to_print modified from hprint http://swensont.epizy.com/ZX81Assembly.pdf?i=1
	;ld hl,$ffff  ; debug check conversion to ascii
    ;ld ($to_print), hl
    
	ld hl,$to_print+$01	
	ld b,2	
hexprint16_loop	
    call waitLCD    
	ld a, (hl)
	push af ;store the original value of a for later
	and $f0 ; isolate the first digit
	rrca
	rrca
	rrca
	rrca        
    call ConvertToASCII
	out (lcdRegisterSelectData), a
    call waitLCD 
	pop af ; retrieve original value of a
	and $0f ; isolate the second digit
    call ConvertToASCII       
	out (lcdRegisterSelectData), a
	dec hl
	djnz hexprint16_loop
	ret	  

hexprint8 		
	push af ;store the original value of a for later
    call waitLCD 
    pop af
    push af ;store the original value of a for later
	and $f0 ; isolate the first digit    
	rrca
	rrca
	rrca
	rrca  
    call ConvertToASCII
	out (lcdRegisterSelectData), a
    call waitLCD 
	pop af ; retrieve original value of a
	and $0f ; isolate the second digit
    call ConvertToASCII       
	out (lcdRegisterSelectData), a
	ret

ConvertToASCII:
    ; assuming the value in register a (0-15) to be converted to ascii
    ; convert the value to its ascii representation
    add a, '0'       ; convert value to ascii character
    cp  ':'        ; compare with ascii '9'
    jr  nc, ConvertToASCIIdoAdd     ; jump if the value is not between 0-9
    jp ConvertToASCII_ret
ConvertToASCIIdoAdd:    
    add a, 7     ; if greater than '9', adjust to ascii a-f
ConvertToASCII_ret:
        
    ret              ; return from subroutine
    

;;; rom "constants"

InitCommandList:
    .db $38,$0e,$01,$06,$ff
BootMessage:
    .db "Z80 AOC2023 day8",$ff
memcheckResultText:
    .db "Memcheck=",$ff    
EnterAddressPromptText
    .db "start/end addr: ",$ff
displayEnterCommandText:    
    .db "enter command:  ",$ff

inputDataLR:
    .db "LLR",$ff
inputDataTab
    .db "AAA","BBB","BBB"
    .db "BBB","AAA","ZZZ"
    .db "ZZZ","ZZZ","ZZZ"
    

    .db 2    
inputDataZZZPos
    .db $0002        
inputDataAAAPos
    .db $0000
inputDataLR_AsNum:   ; this will make it a lot easier!
    .db 0,0,1        ; -1 = L, 1 = R
inputDataMAX_LR:  ; this is the same as the last value in the previous location of inputDataLR_AsNum
inputDataTab_AsNum
    .db 0,1,1
    .db 1,0,2
    .db 2,2,2       
    
    
;;; ram variables    
    .org RAM_START
    
result:
    .db $0000
currentPosInLR:    
    .db $0000   
maxLRIndex:    
    .db $0000       
RAM_MAX_VAR:
    .dw $ffff
POST_RESULT:    
    .dw $ffff    
to_print:
    .dw $0000
commandFound:
    .db $00
#END

