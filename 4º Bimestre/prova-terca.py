class GameProva:
    def repeticao(self, lista):
        for k, v in lista.items():
            while True:
                reposta = str(input(f'\n{k}: ')).lower().strip()
                if reposta == v:
                    print('Acertou!')
                    self.tentativa = 3
                    break
                else:
                    print('Errado!')
                    print(f'Resposta: {v}')

    def espanhol_profissoes(self):
        profissoes = {
            'jogador de futebol' : 'futbolista',
            'ator' : 'actor',
            'atriz' : 'actriz',
            'cantor' : 'cantante',
            'escritor' : 'escritor',
            'pintor' : 'pintor',
            'desenhista' : 'dibujante',
            'cartunista1' : 'dibujante',
            'cartunista2' : 'diseñador',
            'cartunista3' : 'caricaturista',
            'comediante' : 'comediante',
            'advogado' : 'abogado',
            'pedreiro' : 'albañil',
            'dono de casa' : 'amo de casa',
            'arquiteto' : 'arquitecto',
            'artesão' : 'artesano',
            'aeromoça1' : 'azafato',
            'aeromoça2' : 'aeromoza',
            'comissário de bordo1' : 'azafato',
            'comissário de bordo2' : 'aeromozo',
            'salva-vidas1' : 'bañero',
            'salva-vidas2' : 'salvavidas',
            'salva-vidas3' : 'guardavidas',
            'gari' : 'barrendero',
            'bombeiro' : 'bombero',
            'caixa1' : 'cajero',
            'caixa2' : 'caja',
            'garçom1' : 'camamero',
            'garçom2' : 'mesero',
            'caminhoneiro' : 'camionero',
            'cantor' : 'cantante',
            'açougueiro' : 'carnicero',
            'carpinteiro' : 'carpintero',
            'chaveiro' : 'cerrajero',
            'motorista' : 'chófer',
            'cientista' : 'científico',
            'cozinheiro' : 'cocinero',
            'delegado' : 'comisaria',
            'zelador' : 'conserje',
            'contador' : 'contable',
            'atleta' : 'deportista',
            'enfermeiro' : 'enfermero',
            'estudante' : 'estudiante',
            'famacêutico' : 'farmacéutico',
            'encanador1' : 'fontanera',
            'encanador2' : 'plomera',
            'fotógrafo' : 'fotógrafo',
            'engenheiro' : 'ingeniero',
            'pesquisador' : 'investigador',
            'jardineiro' : 'jardinero',
            'juiz' : 'juez',
            'mecânico' : 'mecánico',
            'médico' : 'médico',
            'músico': 'músico',
            'babá' : 'niñero',
            'dentista' : 'odontólogo',
            'padeiro' : 'panadero',
            'confeiteiro' : 'pastelera',
            'cabeleireiro' : 'peluquera',
            'jornalista' : 'periodista',
            'policial' : 'policia',
            'porteiro' : 'portero',
            'professor' : 'profesor',
            'psicólogo' : 'psicólogo',
            'repóter' : 'reportera',
            'alfaiate' : 'sastre',
            'alfaiate' : 'modisto',
            'costureira' : 'costurera',
            'costureira' : 'mosdista',
            'secretário' : 'secretario',
            'criado' : 'sirviento',
            'empregado' : 'sirviento',
            'doméstico' : 'sirviento',
            'taxista' : 'taxista',
            'vendedor' : 'vendedor',
            'sapateiro' : 'zapatero'
        }
        self.repeticao(profissoes)

    def espanhol_verbo_ser(self):
        conjugacao = {
            'yo' : 'soy',
            'tú' : 'eres',
            'él / ella / usted' : 'es',
            'nosotros (as)' : 'somos',
            'vosotros (as)' : 'sois',
            'ellos / ellas / ustedes' : 'son'
        }

        self.repeticao(conjugacao)

    def ingles_partes_corpo(self):
        parte_corpo = {
            # Marcados (Importantes)
            'cabeça' : 'head',
            'pescoço' : 'neck',
            'nariz' : 'nose',
            'boca' : 'mouth',
            'lábios' : 'lips',
            'corpo' : 'body',
            'tórax' : 'chest',
            'orelha' : 'ear',
            'olho' : 'eye',
            'pé' : 'foot',

            # Outros (Complementares)
            'testa' : 'forehead',
            'tronco' : 'torso',
            'cintura' : 'waist',
            'costas' : 'back',
            'pernas' : 'leg',
            'cabelo' : 'hair',
            'língua' : 'tangue',
            'dentes' : 'teeth',
            'bochechas' : 'cheeks',
            'ombro' : 'shoulden',
            'braço' : 'arm',
            'cotovelo' : 'elbow',
            'coxa' : 'thing',
            'joelho' : 'knee',
            'palpebra' : 'eyelids',
            'cílios' : 'eyelashes',
            'sobrancelha' : 'eyebrowns',
            'queixo' : 'chim',
            'rosto' : 'face',
            'nuca' : 'nape',
            'mão' : 'hand',
            'dedos' : 'fingers',
            'barriga' : 'belly',
            'pés' : 'feet',
            'dedos do pé' : 'toes', 
        }

        self.repeticao(parte_corpo)

    def ingles_to_be_presente(self):
        presente = {
            'i' : 'am',
            'you' : 'are',
            'he' : 'is',
            'she' : 'is',
            'it' : 'is',
            'we' : 'are',
            'you' : 'are',
            'they' : 'are'
        }
        
        self.repeticao(presente)

    def ingles_to_be_passado(self):
        passado = {
            'i' : 'was',
            'you' : 'were',
            'he' : 'was',
            'she' : 'was',
            'it' : 'was',
            'we' : 'were',
            'you' : 'were',
            'they' : 'were'
        }

        self.repeticao(passado)

    def ingles_emocoes(self):
        emocoes = {
            'feliz' : 'happy',
            'tristeza' : 'sad',
            'animado' : 'excited',
            'bravo' : 'angry',
            'confuso' : 'confused',
            'preocupado' : 'warried',
            'confiante' : 'confident',
            'estressado' : 'stressed',
            'engraçado' : 'funny'
        }
        self.repeticao(emocoes)

    def ingles_prepo_local(self):
        prepo_local = {
            'Usado para regiões: bairro, cidade, país, continentes, estados' : 'in',
            'Usado para referenciar local' : 'on',
            'Usado para endereço completo' : 'at'
        }

        self.repeticao(prepo_local)

    def ingles_prepo_tempo(self):
        prepo_tempo = {
            'Usado para períoos diurnos' : 'in',
            'Usado para refenciar a semana' : 'on',
            'Usado para tudo referente a horário, mais periodo da noite' : 'at'
        }

        self.repeticao(prepo_tempo)

game = GameProva()

op = int(input('Escolha:\n[1] Espanhol: Profissões\n[2] Espanhol: Verbo "ser"\n[3] Inglês: Partes do Corpo\n[4] Inglês: To Be Presente\n[5] Inglês To Be Passado\n[6] Inglês: Emoções\n[7] Inglês: Preposição Local\n[8] Inglês: Preposição tempo\n: '))

if op == 1:
    game.espanhol_profissoes()
elif op == 2:
    game.espanhol_verbo_ser()
elif op == 3:
    game.ingles_partes_corpo()
elif op == 4:
    game.ingles_to_be_presente()
elif op == 5:
    game.ingles_to_be_passado()
elif op == 6:
    game.ingles_emocoes()
elif op == 7:
    game.ingles_prepo_local()
elif op == 8:
    game.ingles_prepo_tempo()   
