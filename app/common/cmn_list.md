# 共通関数

## 共通関数作成時の注意点
tracebackをimportし、エラー時には\n{tb}のように記載し出力させること。
        ```
        tb = traceback.format_exc()
        print(f"{cmn_msg.ERR_MSG}ここにエラーメッセージ\n{tb}")
        ```

## 共通関数リスト
<dl>
  <dt>cmn_msg</dt>
  <dd>メッセージ出力の際の</dd>
  <dt>cmn_session_db</dt>
  <dd>DBへの接続、切断をする</dd>
</dl>
