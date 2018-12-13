#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class smtp_email_client(object):
    def __init__(self):
        self.smtp_server = None

    def set_smtp_params(self, smtp_server_address, smtp_port, email_from, email_from_password):
        self.smtp_server_address = smtp_server_address
        self.smtp_server_port = smtp_port

        self.smtp_server_user = email_from
        self.smtp_server_password = email_from_password

    def initenv(self):
        """
        初始化登录
        :return:
        """
        if self.smtp_server is None:
            self.smtp_server = smtplib.SMTP(self.smtp_server_address, self.smtp_server_port)
            self.smtp_server.ehlo()
            self.smtp_server.login(self.smtp_server_user, self.smtp_server_password)

    def clearenv(self):
        """
        退出登录
        :return:
        """
        if self.smtp_server:
            self.smtp_server.quit()

    def make_email_message(self, subject, html, email_address):
        """
        生成邮件信息
        :param subject:
        :param html:
        :param email_address:
        :return:
        """
        message = MIMEMultipart('')
        message['From'] = self.smtp_server_user
        message['To'] = ", ".join(email_address)
        message['Cc'] = ""
        message['Subject'] = subject
        msg_text = MIMEText(html, 'html', 'utf-8')
        message.attach(msg_text)
        return message

    def send_email(self, email_message, email_address):
        """
        发送邮件
        :param server:
        :param email_message:
        :param email_address:
        :return:
        """
        self.smtp_server.sendmail(self.smtp_server_user, email_address, email_message.as_string())


