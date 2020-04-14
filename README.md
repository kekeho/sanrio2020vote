# 2020年サンリオキャラクター大賞 一括投票

[2020年サンリオキャラクター大賞](https://ranking.sanrio.co.jp/)で確実に推しに投票するため, 一括投票スクリプトを作成した.  

## 準備

### 1. 推しと自分の情報を登録

[vote.json](vote.json)に押しキャラと年齢・性別・都道府県を登録しておく

#### characters: array[string]

投票したいキャラクター名を(複数)指定.  
正式名称及びエントリーしているかどうかは, 公式サイトで確認のこと.

#### age: int

年齢.

#### gender: string

性別. 公式サイトの表記に準じる.  
以下の選択肢が存在する.  

- 男性
- 女性
- 不明・その他

#### pref: string

お住まいの都道府県.  
公式サイトの表記に準じる.  
海外などの場合は「不明・その他」

### 2. 依存関係ソフトウェアを用意

- docker
- docker-compose

### 3. Build

```sh
$ docker-compose build
```

## 投票

ルール上, 一日1回まで.

```sh
$ docker-compose up
```

時間が経つと, 投票が完了する.  
voted_{推し名}_{日付}.pngというスクリーンショットが保存され, 投票結果が確認できる.


## おねがい

絶対に悪用しないでください.  
悪用して票をかさ増しして, 何が楽しいんですか? 推しが泣いちゃうよ.

## 関連リンク

- [2020年サンリオキャラクター大賞](https://ranking.sanrio.co.jp/)
- [サンリオキャラクター大賞とは](https://ranking.sanrio.co.jp/about/)

## LICENSE

[MIT LICENSE](https://github.com/kekeho/sanrio2020vote/blob/master/LICENSE)
