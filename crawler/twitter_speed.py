__author__ = 'uolter'


from utils import api_init, mongodb
from datetime import datetime, timedelta
import time
import logging
import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(settings.fh)


DEEP_PAST_HOURS = 24
MAX_POST_X_PAGE = 100


hours_ago = datetime.today() - timedelta(hours = DEEP_PAST_HOURS)



def search(term):

    api = api_init.api

    return api.GetSearch(term,
        geocode=None,
        since_id=None,
        max_id=None,
        until=None,
        per_page=MAX_POST_X_PAGE,
        page=1,
        lang=None,
        show_user="false")


def get_speed(result):

    start = end = minutes = None

    # compute the speed:
    if len(result) > 0:
        # Mon, 11 Feb 2013 17:40:50 +0000

        npost = 0 # number of post to consider

        for r in result:
            created_at = datetime.strptime(r.created_at, '%a, %d %b %Y %H:%M:%S +0000')

            if created_at >= hours_ago:
                npost += 1

                if start is None or created_at <= start:
                    start = created_at
                if end is None or created_at >= end:
                    end = created_at

        minutes = (time.mktime(end.timetuple()) - time.mktime(start.timetuple())) / 60
        speed = float( npost / float(minutes))
        acceleration = float(speed) / float(minutes)

        return start, end, speed, acceleration


if __name__ == '__main__':

    
    logger.info('Start')
    

    classification = {}
    
    for i in settings.search_for:

        logger.info('searching for %s' %i)

        result = search(i)
        
        start, end , speed , acceleration = get_speed(result)
        
        logger.debug('messages %d, => speed %f, acceleration %f' %(len(result), speed, acceleration))

        classification[i] = (speed, acceleration)

    mongodb.save(classification)

    logger.info('#' * 50)
    
    for key, value in sorted(classification.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        logger.info( "%s: %s" % (key, value))
    
    logger.info( '#' * 50)
