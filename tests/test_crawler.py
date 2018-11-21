import unittest
from selenium import webdriver

from askfmcrawler import Crawler, Article, User


class CrawlerTest(unittest.TestCase):

    def setUp(self):
        user = User('@uehara1414test', 'uehara')
        self.expected_articles = [
            Article("151023105015", user, "バナナって水に浮く?", "沈みそう"),
            Article("151023102711", user, "他の惑星にも人間は住んでいる?", "住んでない確率が高い"),
            Article("151023102199", user, "あなたを一番よく知っている人は誰ですか?", "自分"),
            Article("151023100919", user, "教室で居眠りしたことある?", "めっちゃある"),
            Article("151023097847", user, "自分らしさは何だと思う？", "説明の難しい真面目と不真面目の同居"),
            Article("151023097079", user, "同性同士でのお付き合いについてどう思いますか?", "好きにして"),
            Article("151023095287", user, "好きなデザートは？", "ガトーショコラ"),
            Article("151023090935", user, "どうして人は宇宙旅行に行きたいのでしょうか?", "インスタ映え"),
            Article("151023089143", user, "1週間一緒に車で旅行に出かけるなら、どこに行きたい?", "九州"),
            Article("151023087607", user, "ハリウッドで一番みんながすごいと思っている人は?", "みんなに聞いて"),
            Article("151023086327", user, "ストレスがたまったら、どうやって解消する？", "ひきこもる"),
            Article("151023085559", user, "長く続く痛みと長く続くかゆみはどっちがいい?", "痛み"),
            Article("151023084279", user, "片方だけになった靴下は何足ある？", "1足"),
            Article("151023075063", user, "最後に見たYouTube動画は？", "PhotoShopの写真加工動画"),
            Article("151023074807", user, "恋愛と戦争では手段を選ばないという言葉に賛成？", "賛成"),
            Article("151023066615", user, "皆さん 石(鉱石)はお好きですか？ 女性の方なら宝石が好きな方が多いと思います", "化石とかちょっとロマン感じる"),
            Article("151023068663", user, "頭がよくするために、大切な記憶を消すことができる?", "たぶんしない"),
            Article("151023065847", user, "赤信号なのに道路を渡ることはある？", "ある"),
            Article("151023064055", user, "動物の王者といえば?", "飼い猫"),
            Article("151023062519", user, "あなたは脳をどのくらい頻繁に使用していますか?", "1日1回くらい"),
            Article("151023055351", user, "支払いをしたくないものがあるとしたらそれはどんなもの?", "学費"),
            Article("151023052791", user, "どんな感じの部屋？", "基本座りっぱなしでオーケー"),
            Article("151023051511", user, "どんなものにお金をかけたい?", "お金稼ぎ"),
            Article("151023049207", user, "あなたから学べることには何がありますか?", "人生の理不尽"),
            Article("151023047159", user, "どのようにして楽しむのが好きですか？", "黙々とゲームする"),
            Article("151023046647", user, "今住んでる町のお気に入りスポットを教えて。", "ラッキーピエロ"),
            Article("151023045367", user, "人はあなたをどう思っていると思いますか?", "困ったやつ"),
            Article("151023044343", user, "晩御飯の時正装するような家庭で育ちたいと思う？", "思わない"),
            Article("151023042807", user, "暑すぎて外にでられない時は何をしてる?", "コード書いてる"),
            Article("151022988535", user, "お気に入りのアスリートは?", "梅原"),
            Article("151022988791", user, "今まで訪れた一番美しかった都市は？", "仙台"),
            Article("151022989047", user, "出会い系アプリで自分を紹介するならなんと紹介する?", "コミッター募集中です"),
            Article("151022989559", user, "朝の支度にはどのくらい時間がかかる？", "10分"),
            Article("151023016695", user, "テスト1", "テスト1の答え")
        ]
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_crawl(self):
        crawler = Crawler(self.driver)
        articles = crawler.crawl_user_questions('uehara1414test')
        self.assertListEqual(articles, self.expected_articles)

    def test_crawl_user(self):
        crawler = Crawler(self.driver)
        users = crawler.crawl_random_users()
        self.assertTrue(len(users) > 10)
        for user in users:
            self.assertEqual(type(user), str)
