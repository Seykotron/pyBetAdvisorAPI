# -*- coding: utf-8 -*-

class Bookmarker:

    def __init__( self, id, name ):
        """
            Class that defines a bookmarker
            id      string  (bookmarker identifier)
            name    string  (bookmarker name)
        """
        self.id     = id
        self.name   = name

class Event:

    def __init__( self, sport_id, sport_name, category_id, category_name, context_id ):
        """
            Class that defines an Event
            sport_id        string  (Id of sport)
            sport_name      string  (Sport name)
            category_id     string  (Id of category (league))
            category_name   string  (Name of category/league)
            context_id      string  (Id of context (tournament))
        """
        self.sport_id       = sport_id
        self.sport_name     = sport_name
        self.category_id    = category_id
        self.category_name  = category_name
        self.context_id     = context_id
