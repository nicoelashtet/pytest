from random import randint
from sys import exit
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("このシーンはまだ設定されていません。")
        print("サブクラスを作成して enter() を実装してください。")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # 最後のシーンも表示する
        current_scene.enter()

class Death(Scene):
    quips = [
        "あなたは死んでしまいました。このゲームが苦手なんですね。",
        "あなたの母親は…もっと賢ければ、誇らしいでしょう。",
        "こんな負け犬。",
        "私の小さな子犬の方がこのゲームを上手にやります。",
        "あなたのお父さんの冗談よりも酷いですね。"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            惑星パーカル25番のゴートン人があなたの宇宙船を侵略し、
            全員の乗組員を殺しました。あなたは最後の生き残りで、
            最後のミッションは武器庫から中性子破壊爆弾を取り、
            ブリッジにそれを設置し、脱出ポッドに乗ってから
            宇宙船を爆破することです。

            武器庫へ走っている途中で、ゴートン人が現れます。
            赤い鱗状の皮膚に、暗い汚れた歯、邪悪なピエロの衣装が
            体中に張り付いています。彼は武器庫への扉を塞いでおり、
            あなたを撃ち殺そうとしています。
            """))

        action = input("> ")

        if action == "撃つ！":
            print(dedent("""
                素早くブラスターを抜き、ゴートン人に向けて発砲します。
                彼のピエロの衣装は体にフィットして動き回り、
                あなたの狙いを外してしまいます。
                レーザーは衣装に命中しますが、彼自身には命中しません。
                これにより、彼の母親が買ってくれたばかりの新しい衣装が
                完全に台無しになり、彼は狂気の怒りに駆られ、
                あなたの顔を連続で撃ち抜き、最後にはあなたを食べてしまいます。
                """))
            return 'death'

        elif action == "かわす！":
            print(dedent("""
                世界クラスのボクサーのようにかわし、すり抜け、
                ゴートン人のブラスターが頭上を通るのをかわします。
                芸術的なかわしの最中、足が滑り、金属の壁に頭を打ちつけ、
                気を失ってしまいます。しばらくして目を覚ますと、
                ゴートン人が頭を踏みつけてあなたを殺します。
                """))
            return 'death'

        elif action == "ジョークを言う":
            print(dedent("""
                幸いにも、学校でゴートン人に対する侮辱を覚えさせられました。
                知っているゴートン人のジョークを言います：
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr.
                ゴートン人は止まり、笑わないようにしようとしますが、
                最終的に爆笑し、動けなくなります。
                彼が笑っている間に、あなたは銃を手に取り、彼の頭に正確に撃ち込み、
                それから武器庫の扉を飛び越えます。
                """))
            return 'laser_weapon_armory'

        else:
            print("計算できません！")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
            武器庫にダイブロールして、しゃがんで部屋をスキャンします。
            隠れているかもしれない他のゴートン人を探しますが、
            何もありません。静寂、あまりにも静かです。立ち上がって、
            部屋の遠い方に走って、中性子爆弾が入ったコンテナを見つけます。
            ボックスにはキーパッドロックがあり、コードが必要です。
            コードを間違えると10回でロックが永遠に閉じ、爆弾を手に入れることができません。
            コードは3桁です。
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[キーパッド]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("ブザァァァァァァ！")
            guesses += 1
            guess = input("[キーパッド]> ")

        if guess == code:
            print(dedent("""
                コンテナがカチッと音を立てて開き、シールが破れ、
                ガスが出ます。中性子爆弾を掴んで、
                右の場所に設置しなければなりません。
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                ロックが最後にブザーを鳴らし、
                機構が溶けるような音がします。そこに座って決めます。
                ゴートン人は彼らの船から船を吹き飛ばし、あなたは死にます。
                """))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            ネトロン破壊爆弾を腕の下に抱えてブリッジに突入し、
            船の制御をしようとしている5人のゴートン人に驚きます。
            それぞれが前の者よりも醜いピエロの衣装を着ています。
            彼らはまだ武器を引き出していません。アクティブな爆弾を
            腕の下に見て、それを起動させたくないようです。
            """))

        action = input("> ")

        if action == "爆弾を投げる":
            print(dedent("""
                パニックになって爆弾をゴートン人の集団に投げつけ、
                ドアに向かって飛びかかります。ちょうどそれを落とす瞬間に、
                ゴートン人が背後から撃ち抜いてきて、あなたは死にます。
                死ぬ間に、別のゴートン人が必死に爆弾を解除しようとしています。
                爆発するとき、彼らが吹き飛ぶのを知りながら死にます。
                """))
            return 'death'

        elif action == "ゆっくりと爆弾を置く":
            print(dedent("""
                ブラスターを爆弾に向け、ゴートン人たちは手を挙げて汗をかき始めます。
                ドアまで後ろに下がり、それから慎重に床に爆弾を置き、
                ブラスターを向けます。その後、ドアを通り抜けて跳び、
                閉めボタンを押し、ロックをブラストしてゴートン人が出られないようにします。
                爆弾が設置されたので、このジャンクに乗って脱出ポッドに走ります。
                """))

            return 'escape_pod'
        else:
            print("計算できません！")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            宇宙船が爆発する前に絶望的に船を駆け抜けます。
            宇宙船にはほとんどゴートン人がいないようで、
            障害物なしで走れます。脱出ポッドのチャンバーに到着し、
            今度はどれを取るか選ばなければなりません。
            いくつかは損傷しているかもしれませんが、
            見る時間はありません。5つのポッドがあります、どれを取りますか？
            """))

        good_pod = randint(1, 5)
        guess = input("[ポッド #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                ポッド {guess} に飛び込んで、イジェクトボタンを押します。
                ポッドは宇宙の虚空に脱出し、そして
                ポッドはハルが破れ、あなたの体をジャムジェリーに押しつぶします。
                """))

            return 'death'
        else:
            print(dedent(f"""
                ポッド {guess} に飛び込んで、イジェクトボタンを押します。
                ポッドは簡単に宇宙にスライドして、下の惑星に向かいます。
                それが惑星に飛ぶ間、あなたは後ろを振り返り、
                宇宙船が明るい星のように爆発し、同時にゴートン人の船を爆破するのを見ます。あなたは勝ちました！
                """))

            return 'finished'

class Finished(Scene):
    def enter(self):
        print("勝ちました！おめでとうございます。")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
