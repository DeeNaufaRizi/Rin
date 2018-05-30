# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from fellyModule.botLogin import *
from fellyModule.botCfg import *
from fellyModule.botFunction import *

def restart_program():
    python2 = sys.executable
    os.execl(python2, python2, * sys.argv)

def shutdown():
    sys.exit()

#Command ini otomatis dijalankan jika restart bot sudah sukses
if restartVar['isRestart'] == True:
    recv=restartVar['restartIn']
    restartVar['isRestart'] = False
    restartVar['restartIn'] = ''
    startTime = time.time()
    print(startTime)
    print('\n'+repr(startTime))
    fellyCfgUpdate()
    cl.sendMessage(recv,'Wayang Restarted')
else:
    if startTime == 0:
        startTime = time.time()
        print(startTime)
        print('\n'+repr(startTime))
        fellyCfgUpdate()

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:            
            # print op
#=========================================================================================================================================#
            # if op.type in OpType._VALUES_TO_NAMES:
            #    print "[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type]))
#=========================================================================================================================================#
            
#=========================================================================================================================================#
            #Owner Command
#=========================================================================================================================================#                
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        #Command dibawah bisa digunakan di grup atau di pm
                        if text.lower() == '.restart wayang':
                            if sender in owner:
                                print("Trying Restart")
                                cl.sendMessage(receiver,"Restarting Wayang")
                                restartVar['isRestart'] = True
                                restartVar['restartIn'] = str(receiver)
                                fellyCfgUpdate()
                                restart_program()
                            else:
                                cl.sendMessage(receiver,"Ngapain cuk??\nOwner doang yg bisa restart :p")
                        elif text.lower() == '.shutdown wayang':
                            if sender in owner:
                                print("Trying Shutdown")
                                cl.sendMessage(receiver,"Preparing Shutdown")
                                time.sleep(randint(0,2))
                                cl.sendMessage(receiver,"Updating Config")
                                time.sleep(randint(0,2))
                                cl.sendMessage(receiver,"See You...")
                                fellyCfgUpdate()
                                shutdown()
                            else:
                                cl.sendMessage(receiver,"Ngapain cuk??\nOwner doang yg bisa restart :p")
                        elif ".getsq" in text.lower():
                            try:
                                x=cl.getJoinedSquares()
                                print(x)
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif ".getsqchat" in text.lower():
                            try:
                                x=cl.getJoinableSquareChats('s3825e0558cc9b4598fb9f557e113eeb1',continuationToken=None, limit=50)
                                print(x)
                            except Exception as e:
                                client.sendMessage(receiver,str(e))
                        elif ".getsqmember" in text.lower():
                            try:
                                x=cl.getSquareMember('p6c69551c4a0cac4f8c3bc2b3c7db948d')
                                print(x)
                            except Exception as e:
                                client.sendMessage(receiver,str(e))
                        elif ".getjoinedgroup" in text.lower():
                            try:
                                x=cl.getGroupIdsJoined()
                                z="List Joined Group\n\n"
                                num=1
                                for y in x:
                                    g = cl.getCompactGroup(y)
                                    print(g)
                                    print("\n")
                                    z += "GName : " +g.name+"\nGId: "+g.id+"\n\n"
                                    num=num+1
                                print("[COMMAND]GET JOINED GROUP EXECUTED\n")
                                cl.sendMessage(receiver,z)
                            except Exception as e:
                                cl.sendMessage(receiver,str(e))
                        elif ".getgroupid " in text.lower():
                            try:
                                gname=text.replace(".getgroupid ","")
                                x=cl.getGroupIdsByName(gname)
                                print("[COMMAND]GET GROUP ID EXECUTED\n")
                                cl.sendMessage(receiver,str(x))
                            except Exception as e:
                                cl.sendMessage(receiver,str(e))
                        elif ".yt " in msg.text.lower():
                            try:
                                query = msg.text.replace(".yt ", "")
                                query = query.replace(" ", "+")
                                x = client.youtube(query)
                                client.sendMessage(receiver, x)
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif ".album " in msg.text.lower():
                            try:
                                query = msg.text.replace(".album ", "")
                                x = getAlbums(query)
                                client.sendMessage(receiver, x)
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif ".track " in msg.text.lower():
                            try:
                                query = msg.text.replace(".track ", "")
                                x = getTracks(query)
                                client.sendMessage(receiver, x)
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif ".lirik " in msg.text.lower():
                            try:
                                query = msg.text.replace(".lirik ", "")
                                x = getLyrics(query)
                                client.sendMessage(receiver, x)
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif ".img " in msg.text.lower():
                            try:
                                query = msg.text.replace(".img ", "")
                                images = client.image_search(query)
                                client.sendImageWithURL(receiver, images)
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif ".meme " in text.lower():
                            try:
                                query = text.replace(".meme ","")
                                qry = query.split("|")
                                font = "impact"
                                templ_id = int(qry[0])
                                templ_id = templ_id-1
                                upper_text = qry[1]
                                lower_text = qry[2]
                                if len(qry) == 4:
                                    font = qry[3]
                                getTemplate=get_memes()
                                template_id=getTemplate[templ_id]['id']
                                genMeme=imgflipMeme(upper_text,lower_text,template_id,font)
                                client.sendImageWithURL(receiver,genMeme['url'])
                            except Exception as e:
                                client.sendMessage(receiver,str(e))
                        elif ".meme_template " in text.lower():
                            try:
                                txt=text.replace(".meme_template ","")
                                x=txt.split("-")
                                start=int(x[0])
                                y=start-1
                                end=int(x[1])
                                if end>100:
                                    client.sendMessage(receiver,"Maksimal 100")
                                else:
                                    getTemplate=get_memes()
                                    listtemp="List Template Meme\n\n"
                                    for i in range(y,end):
                                        a=i+1
                                        listtemp += str(a) + " . " + getTemplate[i]['name'] + "\n"
                                    client.sendMessage(receiver,listtemp)
                            except Exception as e:
                                client.sendMessage(receiver,str(e))
                        elif ".view_template " in text.lower():
                            try:
                                txt=text.replace(".view_template ","")
                                x=int(txt)
                                if x>100:
                                    client.sendMessage(receiver,"Maksimal 100")
                                else:
                                    x=x-1
                                    getTemplate=get_memes()
                                    templateUrl=getTemplate[x]['url']
                                    client.sendImageWithURL(receiver,templateUrl)
                            except Exception as e:
                                client.sendMessage(receiver,str(e))
                        elif 'say:' in msg.text.lower():
                            try:
                                isi = msg.text.lower().replace('say:','')
                                tts = gTTS(text=isi, lang='id', slow=False)
                                tts.save('temp.mp3')
                                client.sendAudio(receiver, 'temp.mp3')
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif 'apakah ' in msg.text.lower():
                            try:
                                txt = ['iya','tidak','bisa jadi']
                                isi = random.choice(txt)
                                tts = gTTS(text=isi, lang='id', slow=False)
                                tts.save('temp2.mp3')
                                client.sendAudio(receiver, 'temp2.mp3')
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif "sytr:" in msg.text:
                            try:
                                isi = msg.text.split(":")
                                translator = Translator()
                                hasil = translator.translate(isi[2], dest=isi[1])
                                A = hasil.text
                                tts = gTTS(text=A, lang=isi[1], slow=False)
                                tts.save('temp3.mp3')
                                client.sendAudio(receiver, 'temp3.mp3')
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif "tr:" in msg.text:
                            try:
                                isi = msg.text.split(":")
                                translator = Translator()
                                hasil = translator.translate(isi[2], dest=isi[1])
                                A = hasil.text                               
                                client.sendMessage(receiver, str(A))
                            except Exception as e:
                                client.sendMessage(receiver, str(e))
                        elif text.lower() in ['.speed','.sp']:
                            start = time.time()
                            client.sendMessage(receiver, "TestSpeed")
                            elapsed_time = time.time() - start
                            client.sendMessage(receiver, "%sdetik" % (elapsed_time))
                        elif text.lower() == '.runtime':
                            client.sendMessage(receiver, "Counting")
                            elapsed_time = time.time() - startTime
                            m, s = divmod(elapsed_time, 60)
                            h, m = divmod(m, 60)
                            d, h = divmod(h, 24)
                            print(("d:h:m:s-> %d:%d:%d:%d" % (d, h, m, s)))
                            client.sendMessage(receiver, "d:h:m:s-> %d:%02d:%02d:%02d" % (d, h, m, s))
                        #Command dibawah hanya untuk didalam grup
                        elif msg.toType == 2:
                            if sender in owner:
                                client.sendChatChecked(receiver, msg_id)
                                contact = client.getContact(sender)
                                if text.lower() in ['me','.me']:
                                    client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                    client.tag(receiver, sender)
                                elif '.gc ' in text.lower():
                                    try:
                                        key = eval(msg.contentMetadata["MENTION"])
                                        u = key["MENTIONEES"][0]["M"]
                                        cname = client.getContact(u).displayName
                                        cmid = client.getContact(u).mid
                                        cstatus = client.getContact(u).statusMessage
                                        cpic = client.getContact(u).picturePath
                                        #print(str(a))
                                        client.sendMessage(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                        client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                        if "videoProfile='{" in str(client.getContact(u)):
                                            client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                        else:
                                            client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
                                elif '.sticker:' in msg.text.lower():
                                    try:
                                        query = msg.text.replace("sticker:", "")
                                        query = int(query)
                                        if type(query) == int:
                                            client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                            client.sendMessage(receiver, 'https://line.me/S/sticker/'+str(query))
                                        else:
                                            client.sendMessage(receiver, 'gunakan key sticker angka bukan huruf')
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
                                elif 'spic' in text.lower():
                                    try:
                                        key = eval(msg.contentMetadata["MENTION"])
                                        u = key["MENTIONEES"][0]["M"]
                                        a = client.getContact(u).pictureStatus
                                        if "videoProfile='{" in str(client.getContact(u)):
                                            client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                        else:
                                            client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
                                elif 'scover' in text.lower():
                                    try:
                                        key = eval(msg.contentMetadata["MENTION"])
                                        u = key["MENTIONEES"][0]["M"]
                                        a = channel.getProfileCoverURL(mid=u)
                                        client.sendImageWithURL(receiver, a)
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
                                elif text.lower() in ['.tagall','.mentionall','.summon','.kimotih']:   
                                        tagall(client,receiver)
                                elif text.lower() in ['.tagadmin','.mentionadmin','.summonadmin','.itteh']:   
                                        tagadmin(client,receiver)
                                elif text.lower() == ".setbotkuy":
                                    group = cl.getGroup(msg.to)
                                    nama = [contact.mid for contact in group.members]
                                    for md in nama:
                                        if md in boten:
                                          wait["joinedBoT"] = str(md)
                                          wait["groupId"] = str(group.id)
                                          fellyCfgUpdate()
                                          cl.sendMessage(msg.to, "Battle of Ten sudah di set")                                         
                                elif text.lower() == ".unsetbotkuy":
                                        wait["joinedBoT"] = ""
                                        wait["groupId"] = ""
                                        fellyCfgUpdate()
                                        cl.sendMessage(msg.to, "Battle of Ten sudah di unset")
                                elif msg.text in [".kuy",".nganu",".join kuy"]: #Panggil Semua Bot
                                    inv=inviteBot(KAC,receiver)
                                    print(inv)
                                    cl.sendMessage(receiver,inv)
                                elif msg.text in [".felly masuk"]: #Panggil Felly ke Group
                                    ad=[cl,ki]
                                    inv=inviteBot(ad,receiver)
                                    print(inv)
                                    cl.sendMessage(receiver,inv)
                                elif text.lower() in [".cabut all",".kabur all",".kaboor all"]: #Bot Ninggalin Group termasuk Bot Induk
                                    ginfo = cl.getGroup(receiver)
                                    try:
                                        ki.leaveGroup(receiver)
                                        kk.leaveGroup(receiver)
                                        kc.leaveGroup(receiver)
                                        ks.leaveGroup(receiver)
                                    except:
                                        pass
                                elif ".setbattle: " in text.lower():
                                    settxt=text.replace(".setbattle: ","")
                                    modetxt=settxt.split(" ")
                                    if modetxt[0] == "auto":
                                        wait["autoBattle"]=True
                                        wait["battleMode"]=modetxt[1]
                                        cl.sendMessage(wait['groupId'],"Auto Battle Mode : ON \nBattle Mode : "+wait['battleMode'])
                                    elif modetxt[0] == "off":
                                        wait["autoBattle"]=False
                                        wait["battleMode"]=""
                                        cl.sendMessage(wait['groupId'],"Auto Battle Mode : OFF \nBattle Mode : None")
                                elif text == '.grAdd':
                                    print("[Command]GroupList Add executing")
                                    if receiver not in grouplist:
                                        grouplist.append(str(receiver))
                                        groupAdmin[str(receiver)]=[]
                                        cl.sendMessage(receiver,"Grup Ditambahkan ke list")
                                        fellyCfgUpdate()
                                    else:
                                        cl.sendMessage(receiver,"Grup sudah ada di list")
                                    print("[Command]GroupList Add executed")
                                elif text == '.grRemove':
                                    print("[Command]GroupList Remove executing")
                                    if receiver in grouplist:
                                        grouplist.remove(receiver)
                                        groupAdmin.pop(str(receiver),None)
                                        if receiver in protectedGroup:
                                            protectedGroup.remove(receiver)
                                        cl.sendMessage(receiver,"Grup Dihapus dari list")
                                        fellyCfgUpdate()
                                    else:
                                        cl.sendMessage(receiver,"Grup tidak ada di dalam list")
                                    print("[Command]GroupList Remove executed")
                                elif text == '.grList':
                                    print("[Command]grouplist executing")
                                    grlist=getGroupList(cl)
                                    cl.sendMessage(receiver,grlist)
                                    print("[Command]grouplist executed")
                                elif "grAdmin add @" in text:
                                    print("[Command]Staff add executing")
                                    targets = getCalonAdmin(KAC,receiver,text)
                                    if targets == []:
                                        cl.sendMessage(receiver,"Contact not found")
                                    else:
                                        for target in targets:
                                            if receiver in grouplist:
                                                if target not in admin:
                                                    if target not in groupAdmin[receiver]:
                                                        try:
                                                            groupAdmin[receiver].append(str(target))
                                                            cl.sendMessage(receiver,"Admin Grup Ditambahkan")
                                                            fellyCfgUpdate()
                                                        except:
                                                            pass
                                                    else:
                                                        cl.sendMessage(receiver,"Existing Group Admin")
                                                else:
                                                    cl.sendMessage(receiver,"Targetnya Admin Wayang Dugem Boss")                                                                   
                                            else:
                                                cl.sendMessage(receiver,"Grup ini belum masuk grouplist")
                                    print("[Command]Staff add executed")
                                elif "grAdmin remove @" in text:
                                    print("[Command]Staff remove executing")
                                    targets = getCalonAdmin(KAC,receiver,text)
                                    if targets == []:
                                        cl.sendMessage(receiver,"Contact not found")
                                    else:
                                        for target in targets:
                                            if receiver in grouplist:
                                                if target in groupAdmin[receiver]:
                                                    try:
                                                        groupAdmin[receiver].remove(target)
                                                        cl.sendMessage(receiver,"Admin Grup Dihapus")
                                                        fellyCfgUpdate()
                                                    except:
                                                        pass
                                                else:
                                                    cl.sendMessage(receiver,"Target not Group Admin")
                                            else:
                                                cl.sendMessage(receiver,"Grup ini belum masuk grouplist")
                                    print("[Command]Staff remove executed")
                                elif text.lower() == '.adminlist':
                                    alist=getAdminList(cl,receiver)
                                    cl.sendMessage(receiver,alist)
                                    print("[Command]Adminlist executed")
                                elif "Admin add @" in text:
                                    print("[Command]Staff add executing")
                                    targets = getCalonAdmin(KAC,receiver,text)
                                    if targets == []:
                                        cl.sendMessage(receiver,"Contact not found")
                                    else:
                                        for target in targets:
                                            if target not in admin:
                                                try:
                                                    admin.append(str(target))
                                                    cl.sendMessage(receiver,"Admin Ditambahkan")
                                                    fellyCfgUpdate()
                                                except:
                                                    pass
                                            else:
                                                cl.sendMessage(receiver,"Existing Admin")
                                    print("[Command]Staff add executed")
                                elif "Admin remove @" in text:
                                    print("[Command]Staff remove executing")
                                    targets = getCalonAdmin(KAC,receiver,text)
                                    if targets == []:
                                        cl.sendMessage(receiver,"Contact not found")
                                    else:
                                        for target in targets:
                                            if target in admin:
                                                try:
                                                    admin.remove(target)
                                                    cl.sendMessage(receiver,"Admin Dihapus")
                                                    fellyCfgUpdate()
                                                except:
                                                    pass
                                            else:
                                                cl.sendMessage(receiver,"Target Not Admin")
                                    print("[Command]Staff remove executed")
                                elif text.lower() == '.help':
                                    helpMenu = helpMessage
                                    helpMenu += helpAdmin+helpOwner
                                    helpMenu += helpFooter
                                    cl.sendMessage(receiver,helpMenu)
                                elif text.lower() == '.updateconfig':
                                    fellyCfgUpdate()
                                    cl.sendMessage(receiver,"Config Updated Successfully")
                                elif text.lower() in ['.ceksider','.cctv','.halosider']:
                                    txt = text.lower()
                                    try:
                                        del cctv['point'][receiver]
                                        del cctv['sidermem'][receiver]
                                        del cctv['cyduk'][receiver]
                                        del cctv['haloSider'][receiver]
                                    except:
                                        pass
                                    cctv['point'][receiver] = msg.id
                                    cctv['sidermem'][receiver] = "Kang CCTV Keciduk Nih"
                                    cctv['cyduk'][receiver]=True
                                    cctv['haloSider'][receiver]=False
                                    if txt=='.halosider':
                                        cctv['haloSider'][receiver]=True
                                elif text.lower() in ['.offread','.ciduk']:
                                    if msg.to in cctv['point']:
                                        cctv['cyduk'][receiver]=False
                                        client.sendMessage(receiver, cctv['sidermem'][msg.to])
                                    else:
                                        client.sendMessage(receiver, "Heh belom di Set")
                                elif text.lower() in ['.resetcctv','.resetsider']:
                                    try:
                                        del cctv['point'][receiver]
                                        del cctv['sidermem'][receiver]
                                        del cctv['cyduk'][receiver]
                                        del cctv['haloSider'][receiver]
                                    except:
                                        pass
                                    cl.sendMessage(receiver,"List CCTV grup ini sudah di reset")
                                elif text.lower() == 'mode:self':
                                    mode = 'self'
                                    fellyCfgUpdate()
                                    client.sendMessage(receiver, 'Mode Public Off')
                                elif text.lower() == 'mode:public':
                                    cek=isBotJoined(cl,Bots,receiver)
                                    resmsg=""
                                    if cek == []:
                                        resmsg='Puclic Mode Activation Failed\nError : Missing Felly'
                                    else:
                                        try:
                                            for ceks in cek:
                                                if ceks == Amid:
                                                    mode = 'public'
                                                    fellyCfgUpdate()
                                                    resmsg='Mode Public ON'
                                                else:
                                                    resmsg='Puclic Mode Activation Failed\nError : Missing Felly'
                                        except Exception as e:
                                            resmsg=str(e)
                                    client.sendMessage(receiver, resmsg)
                                elif ".setprotect:" in text.lower():
                                    try:
                                        prot=text.replace(".setprotect:","")
                                        if prot.lower()=='on':
                                            if receiver in grouplist:
                                                if receiver not in protectedGroup:
                                                    protectedGroup.append(str(receiver))
                                                    fellyCfgUpdate()
                                                    cl.sendMessage(receiver,"Done : Protection ON")
                                                else:
                                                    cl.sendMessage(receiver,"This Group has been protected")
                                            else:
                                                cl.sendMessage(receiver,"Grup nya masukin list dlu dong om")
                                        elif prot.lower()=='off':
                                            if receiver in grouplist:
                                                if receiver in protectedGroup:
                                                    protectedGroup.remove(receiver)
                                                    fellyCfgUpdate()
                                                    cl.sendMessage(receiver,"Done : Protection OFF")
                                                else:
                                                    cl.sendMessage(receiver,"This Group not protected")
                                            else:
                                                cl.sendMessage(receiver,"Group ini ga ada di list om")
                                        else:
                                            cl.sendMessage(receiver,"Invalid Parameter")
                                    except Exception as e:
                                        cl.sendMessage(receiver,str(e))
                                elif ".autoadd:" in text.lower():
                                    try:
                                        prot=text.replace(".autoadd:","")
                                        if prot.lower()=="on":
                                            if wait["autoAdd"] == True:
                                                cl.sendMessage(receiver,"Auto Add Already ON")
                                            elif wait["autoAdd"] == False:
                                                wait["autoAdd"] = True
                                                fellyCfgUpdate()
                                                cl.sendMessage(receiver,"Done : Auto Add ON")
                                        elif prot.lower()=="off":
                                            if wait["autoAdd"] == True:
                                                wait["autoAdd"] = False
                                                fellyCfgUpdate()
                                                cl.sendMessage(receiver,"Done : Auto Add OFF")
                                            elif wait["autoAdd"] == False:
                                                cl.sendMessage(receiver,"Auto Add Already OFF")
                                        else:
                                            cl.sendMessage(receiver,"Invalid Parameter")
                                    except Exception as e:
                                        cl.sendMessage(receiver,str(e))
                                elif ".bigaj:" in text.lower():
                                    try:
                                        prot=text.replace(".bigaj:","")
                                        if prot.lower()=="on":
                                            if wait["bigAj"] == True:
                                                cl.sendMessage(receiver,"Already ON")
                                            elif wait["bigAj"] == False:
                                                wait["bigAj"] = True
                                                cl.sendMessage(receiver,"Done")
                                        elif prot.lower()=="off":
                                            if wait["bigAj"] == True:
                                                wait["bigAj"] = False
                                                cl.sendMessage(receiver,"Done")
                                            elif wait["bigAj"] == False:
                                                cl.sendMessage(receiver,"Already OFF")
                                        else:
                                            cl.sendMessage(receiver,"Invalid Parameter")
                                    except Exception as e:
                                        cl.sendMessage(receiver,str(e))
                                elif ".refresh_battle" in text.lower():
                                    try:
                                        txt="/refresh"
                                        ki.sendMessage(wait["joinedBoT"],(txt))
                                        kc.sendMessage(wait["joinedBoT"],(txt))
                                        kk.sendMessage(wait["joinedBoT"],(txt))
                                        ks.sendMessage(wait["joinedBoT"],(txt))
                                    except Exception as e:
                                        cl.sendMessage(receiver,str(e))
                                elif ".cekmember @" in text.lower():
                                    _name = text.replace(".cekmember @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = cl.getGroup(receiver)
                                    targets = ''
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets=g.mid
                                    if targets == '':
                                        result="Tidak Ditemukan....."
                                    else:
                                        if targets not in owner or admin or groupAdmin[receiver]:
                                            cl.sendMessage(receiver,"Target adalah Member")
                                        else:
                                            cl.sendMessage(receiver,"Target adalah Admin")
                                elif text.lower() in [".oqr",".openqr",".bukaqr",".ourl"]:
                                    oqr=openQr(cl,receiver)
                                    cl.sendMessage(receiver,oqr)
                                elif text.lower() in [".cqr",".closeqr",".curl",".tutupqr"]:
                                    cqr=closeQr(cl,receiver)
                                    cl.sendMessage(receiver,cqr)
                                elif text.lower() in [".gurl",".groupurl"]:
                                    gu=gurl(cl,receiver)
                                    cl.sendMessage(receiver,gu)
                                elif "nk " in text.lower():
                                    nk=nameKick(cl,msg)
                                    cl.sendMessage(receiver,nk)
                            else:
                                client.sendMessage(receiver,"Owner Only Kakak")
                except Exception as e:
                    client.log("[SEND MESSAGE] ERROR : " + str(e))
            elif op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if sender in boten:
                        # print msg
                        # print "\n"
                        # group=cl.getGroup(msg.to)
                        if receiver == wait["groupId"]:
                            if msg.contentType == 4:
                                print("Joined BoT : "+wait["joinedBoT"]+"\n")
                                print("Group ID : "+wait["groupId"]+"\n")
                                print("msg from boten ok")
                                print(json.dumps(msg.contentMetadata))
                                print("\n")
                                mes=str(msg.contentMetadata)
                                mes=mes.replace("{","")
                                mes=mes.replace("}","")
                                # txt=mes.split(":")
                                mesindex=mes.find('/join')
                                if mesindex == -1:
                                    pass
                                else:
                                    temp_txt=mes[mesindex:]
                                    arr_temp=temp_txt.split(" ")
                                    txt=arr_temp[0]+" "+arr_temp[1]
                                    print(txt)
                                    print("\n\n")
                                    time.sleep(randint(1,10))
                                    ki.sendMessage(wait["joinedBoT"],(txt))
                                    kc.sendMessage(wait["joinedBoT"],(txt))
                                    kk.sendMessage(wait["joinedBoT"],(txt))
                                    ks.sendMessage(wait["joinedBoT"],(txt))
                                    if wait['autoBattle']==False:
                                        cl.sendMessage(wait["joinedBoT"],(txt))
                            elif msg.contentType == 0:
                                if msg.toType == 2:
                                    if "Semua musuh sudah mati.\nTim " in msg.text:
                                        if wait["autoBattle"] == True:
                                            print(msg.text)
                                            print("\nBoten Read\n")
                                            cl.sendMessage(msg.to, "bentar ya, auto reset 5 detik lg... itteh itteh kimotih")
                                            time.sleep(5)
                                            cl.sendMessage(msg.to, "/resetbot")
                                            time.sleep(2)
                                            cl.sendMessage(msg.to, ".tagall")
                                        else:
                                          print(msg.text)
                        elif wait["bigAj"] == True:
                            if msg.contentType == 4:
                                print(json.dumps(msg.contentMetadata))
                                mes=str(msg.contentMetadata)
                                mes=mes.replace("{","")
                                mes=mes.replace("}","")
                                # txt=mes.split(":")
                                mesindex=mes.find('/join')
                                if mesindex == -1:
                                    pass
                                else:
                                    temp_txt=mes[mesindex:]
                                    arr_temp=temp_txt.split(" ")
                                    txt=arr_temp[0]+" "+arr_temp[1]
                                    print(txt)
                                    print("\n\n")
                                    time.sleep(randint(1,10))
                                    cl.sendMessage(sender,(txt))
                            else:
                                pass
                        else:
                            pass
                    else:
                        if msg.toType == 4:
                            print(msg)
                        elif mode == "public":
                            if receiver in grouplist:
                                if msg.contentType == 0:
                                    if msg.toType == 2:
                                        # if receiver in grouplist
                                        if text.lower() == '.adminlist':
                                            alist=getAdminList(ki,receiver)
                                            ki.sendMessage(receiver,alist)
                                            print("[Command]Adminlist executed")
                                        elif text.lower() in ['.tagadmin','.mentionadmin','.summonadmin','.itteh']:   
                                            tagadmin(ki,receiver)
                                        elif text.lower() == '.help':
                                            helpMenu=helpMessage
                                            if sender in owner:
                                                helpMenu += helpAdmin+helpOwner
                                            elif sender in admin:
                                                helpMenu += helpAdmin
                                            helpMenu+=helpFooter
                                            ki.sendMessage(receiver,helpMenu)
                                        else:
                                            if sender in admin or groupAdmin[receiver]:
                                                if text.lower() in ['.tagall','.mentionall','.summon']:
                                                    print("\nProcessing Tagall\n")
                                                    tagall(ki,receiver)
                                            else:
                                                pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                except Exception as e:
                    client.log("[READ MESSAGE] ERROR : " + str(e))
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                if cctv['haloSider'][op.param1] == True:
                                    client.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                                else:
                                    pass
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
            # if op.type == 19: #bot Ke Kick
            #     if op.param3 in mid:
            #         if op.param2 in Bots:
            #             pass 
            #         elif op.param2 in admin:
            #             pass
            #         elif op.param2 in groupAdmin[op.param1]:
            #             pass
            #         else:
            #             try:
            #                 print("ki Take Action")
            #                 ki.kickoutFromGroup(op.param1,[op.param2])
            #                 inviteBot([ki,cl],op.param1)
            #             except:
            #                 print("cl Exception Take Action")
            #                 cl.kickoutFromGroup(op.param1,[op.param2])
            #                 inviteBot([cl,ki],op.param1)
            else:
                pass       
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
